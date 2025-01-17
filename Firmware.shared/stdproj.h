#pragma once

#define STDPROJ_H__INCLUDED__

#include <bmt.h>

//#define OPT_IMPLEMENT_TEST_DB

#ifdef __cplusplus

#include <platform.h>

#if 0
#if defined(BLUEPILL_V1)
#	include "bluepill-v1/platform.h"
#elif defined(BLUEPILL_V2)
#	include "bluepill-v2/platform.h"
#elif defined(NUCLEO32_L432KC)
#	include "nucleo-l432kc/platform.h"
#elif defined(NUCLEO32_G431KB)
#	include "nucleo-g431kb/platform.h"
#else
#	error Please define the platform for debugging
#endif
#endif

#ifndef OPT_JTAG_USING_SPI
#error OPT_JTAG_USING_SPI definition is required for every platform
#endif

/// A stop watch object
typedef Timer::MicroStopWatch<TickTimer> StopWatch;

#ifdef OPT_USART_ISR
/// Defines a dual FIFO buffer for GDB UART port
typedef UartFifo<UsartGdbSettings, 256, 64> UsartGdbBuffer;
/// The UART driver using interrupts
typedef UsartIntDriverModel<UsartGdbBuffer> UsartGdbDriver;
/// Singleton for the GDB UART
extern UsartGdbDriver gUartGdb;
#endif


typedef SwoChannel<0> Trace_;
typedef SwoChannel<1> Error_;
#if DEBUG
typedef SwoChannel<2> Debug_;
#else
typedef SwoDummyChannel Debug_;
#endif
typedef SwoTraceSetup <SysClk, SwoProtocol::kAsynchronous, 720000, Trace_, Error_, Debug_> SwoTrace;
// A stream object for the trace output
typedef OutStream<Trace_> Trace;
typedef OutStream<Error_> Error;
typedef OutStream<Debug_> Debug;

#ifdef DEBUG
#	define WATCHPOINT()		__NOP()
#else
#	define WATCHPOINT()		
#endif

//! XML is currently disabled on MSP430 GDB
#define OPT_MEMORY_MAP	0

#endif		// __cplusplus
