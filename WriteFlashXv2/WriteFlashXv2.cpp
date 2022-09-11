#include <msp430.h>
#include <stdint.h>
#include "../FuncletsInterface/Interface.h"

#ifndef __MSP430X_LARGE__
// Please make sure that compilation parameter produces 20-bit pointers
#error "Please setup Compiler with the -mlarge option"
#endif

void WriteFlashXv2(WriteCtrlXv2* ctrl) asm("main") __attribute__((naked, noreturn, optimize("Os"), lower));

/*
** This code is intended to run on RAM and writes the flash memory
** Parameter ctrl is passed on R12.
** Stack pointer needs to be initialized and have 4 bytes space
*/
void WriteFlashXv2(WriteCtrlXv2* ctrl)
{
	// Stop WDT
	WDTCTL = WDTPW | WDTHOLD;
	// Indicates driver start
	SYSJMBO1 = 0xABAD;
	SYSJMBO0 = 0xBABE;
	// Backup Flash configuration (with password restore)
	ctrl->reg_bak1_ = FCTL1 ^ 0x3300;
	ctrl->reg_bak3_ = FCTL3 ^ 0x3300;

	// Flash busy?
	while (FCTL3 & BUSY)
		;

	// Read and compare
	FCTL3 = ctrl->unlock_;
	// LOCKA can be toggled, never set (see docs)
	if ((uint8_t)FCTL3 != (uint8_t)ctrl->unlock_)
		FCTL3 = ctrl->unlock_ | LOCKA;

	// Flash write word access
	FCTL1 = FWKEY + WRT;
	// Disable auto-clear feature, 16-bit mode
	SYSJMBC = JMBCLR0OFF + JMBMODE;
	// Repeat for all expected words
	do
	{
		// Wait for data available in the mailbox?
		while ((SYSJMBC & JMBIN0FG) == 0)
			;
		// Move data to memory
		*ctrl->addr_++ = SYSJMBI0;
		SYSJMBC &= ~JMBIN0FG;
		// Wait for flash operation
		while (FCTL3 & BUSY)
			;
	}
	while (--ctrl->cnt_);

	// Lock flash again
	FCTL1 = ctrl->reg_bak1_;
	FCTL3 = ctrl->reg_bak3_;
	// Toggle if LOCKA state does not match
	if ((uint8_t)FCTL3 != (uint8_t)ctrl->reg_bak3_)
		FCTL3 = ctrl->reg_bak3_ | LOCKA;

	// Signal end of function
	SYSJMBO1 = 0xCAFE;
	SYSJMBO0 = 0xBABE;

	// Loop forever, until controller takes control
#if 0
	// Removed, since compiler ignores the -fPIC/-fPIE compiler flag and generates absolute jump, 
	// instead of the relative jump
	for (;;)
	{
	}
#else
	__asm volatile(
	".FOREVER:\r\n"
		"	jmp	.FOREVER\r\n"
		);
#endif
}
