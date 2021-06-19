#! py -3
# -*- coding: LATIN_1 -*-

import os, sys
import xml.etree.ElementTree as ET
import copy

NAME_PREFIX_TAB = ( \
	("MSP430SL5438A", 'a' )
	, ("MSP430FE42",  'b')
	, ("MSP430AFE2",  'c')
	, ("RF430FRL15",  'd')
	, ("MSP430F67",   'e')
	, ("MSP430FG4",   'f')
	, ("MSP430FG6",   'g')
	, ("MSP430FR2",   'h')
	, ("MSP430FR4",   'i')
	, ("MSP430FR5",   'j')
	, ("MSP430FR6",   'k')
	, ("MSP430F1",    'l')
	, ("MSP430F2",    'm')
	, ("MSP430F4",    'n')
	, ("MSP430F5",    'o')
	, ("MSP430F6",    'p')
	, ("MSP430FW",    'q')
	, ("MSP430G2",    'r')
	, ("MSP430C",     's')
	, ("MSP430L",     't')
	, ("RF430F5",     'u')
	, ("CC430F",      'v')
	, ("MSP430",      'w')
	)

def ChipNameCompress(s):
	# This is necessarily sorted from larger string to shorter
	for f,k in NAME_PREFIX_TAB:
		if s.startswith(f):
			p2 = s[len(f):]
			#if not p2[0].isdigit():
			#	print (s)
			return k + p2
	#print (s)
	return s

def mk_identifier(s):
	tmp = ''
	for ch in s:
		if not tmp:
			if ch.isalpha() or (ch == '_'):
				tmp += ch
			else:
				tmp += '_'
		elif ch.isalnum() or (ch == '_'):
			tmp += ch
		else:
			tmp += '_'
	return tmp

def extract_lo(str):
	w = int(str, 0) & 0xFF
	return hex(w)

def extract_hi(str):
	w = (int(str, 0) >> 8) & 0xFF
	return hex(w)

def DoHfileStart(fh=sys.stdout):
	fh.write("""/////////////////////////////////////////////////////////////////////////////////////
// THIS FILE WAS AUTOMATICALLY GENERATED BY **ExtraChipInfo.py** SCRIPT!
// DO NOT EDIT!
/////////////////////////////////////////////////////////////////////////////////////
// Information extracted from:
// MSPDebugStack_OS_Package_3_15_1_1.zip\DLL430_v3\src\TI\DLL430\DeviceDb\devicedb.h
/////////////////////////////////////////////////////////////////////////////////////

/*
 * C:\MSP430\mspdebugstack\DLL430_v3\src\TI\DLL430\DeviceDb\devicedb.h
 *
 * Copyright (C) 2020 Texas Instruments Incorporated - http://www.ti.com/
 *
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *    Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 *    Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the
 *    distribution.
 *
 *    Neither the name of Texas Instruments Incorporated nor the names of
 *    its contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 *  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 *  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 *  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 *  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 *  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#pragma once

namespace ChipInfoDB {

//! Signals that start address field of the record is undefined
#define NO_MEM_START	0x000FFFFF	// an odd value is impossible
//! Signals the the main ID field of the record is undefined
#define NO_MCU_ID0		0xFFFF
//! Signals the the ID info field byte of the record is undefined
#define EMPTY_INFO_SLOT	0xFF

#pragma pack(1)

// Memory class
enum MemoryClass : uint32_t
{
	kClasMain
	, kClasRam
	, kClasRam2
	, kClasTinyRam
	, kClasLeaRam
	, kClasInfo
	, kClasCpu
	, kClasIrVec
	, kClasLcd
	, kClasEem
	, kClasBootCode
	, kClasBootCode2
	, kClasBsl
	, kClasBsl2
	, kClasMidRom
	, kClasUsbRam
	, kClasPeripheral8bit
	, kClasPeripheral16bit
	, kClasPeripheral16bit1
	, kClasPeripheral16bit2
	, kClasPeripheral16bit3
	, kClasUssPeripheral
	, kClasLeaPeripheral
	, kClasLib
	, kClasMax_
};

// Type of memory
enum MemoryType : uint32_t
{
	kNullMemType
	, kRegister
	, kFlash
	, kRam
	, kRom
	, kMemTypeMax
};

// Type of memory access
enum MemAccessType : uint32_t
{
	kNullMemAccess
	, kBootcodeRomAccess
	, kBslRomAccess
	, kBslRomAccessGR
	, kBslFlashAccess
	, kFlashMemoryAccess2ByteAligned
	, kInformationFlashAccess
	, kFramMemoryAccessBase
	, kFramMemoryAccessFRx9
	, kTinyRandomMemoryAccess
	, kLockableRamMemoryAccess
	, kUsbRamAccess
	, kRegisterAccess5xx
	, kMemAccessMax
};

// PSA Support
enum PsaType : uint16_t
{
	kNullPsaType
	, kRegular
	, kEnhanced
	, kPsaMax
};

// Architecture of the CPU
enum CpuArchitecture : uint16_t
{
	kNullArchitecture
	, kCpu
	, kCpuX
	, kCpuXv2
};

// EEM type
enum EemType : uint8_t
{
	kNullEem
	, kEMEX_LARGE_5XX
	, kEemMax_
};

// Bit size of the CPU or Peripheral
enum BitSize : uint32_t
{
	kNullBitSize
	, k8
	, k16
	, k20
};

// Enumeration that specifies the address start of a memory block
enum AddressStart : uint32_t
{
	kStart_None
	, kStart_0x0
	, kStart_0x6
	, kStart_0x20
	, kStart_0x90
	, kStart_0x100
	, kStart_0x200
	, kStart_0xa80
	, kStart_0xb00
	, kStart_0xc00
	, kStart_0xe00
	, kStart_0xf00
	, kStart_0x1000
	, kStart_0x1100
	, kStart_0x1800
	, kStart_0x1900
	, kStart_0x1a00
	, kStart_0x1c00
	, kStart_0x1c80
	, kStart_0x1e00
	, kStart_0x2000
	, kStart_0x2100
	, kStart_0x2380
	, kStart_0x2400
	, kStart_0x2500
	, kStart_0x2c00
	, kStart_0x3100
	, kStart_0x4000
	, kStart_0x4400
	, kStart_0x5c00
	, kStart_0x6000
	, kStart_0x6c00
	, kStart_0x8000
	, kStart_0xa000
	, kStart_0xa400
	, kStart_0xc000
	, kStart_0xc200
	, kStart_0xc400
	, kStart_0xe000
	, kStart_0xe300
	, kStart_0xf000
	, kStart_0xf100
	, kStart_0xf800
	, kStart_0xf840
	, kStart_0xf880
	, kStart_0xfc00
	, kStart_0xfe00
	, kStart_0xffe0
	, kStart_0xc0000
	, kStart_0xf0000
	, kStart_0xf8000
	, kStart_0xfac00
	, kStart_0xffc00
	, kStart_Max_
};

// Enumeration that specifies the size of a memory block
enum BlockSize : uint32_t
{
	kSize_None
	, kSize_0x6
	, kSize_0xd
	, kSize_0x10
	, kSize_0x15
	, kSize_0x1a
	, kSize_0x20
	, kSize_0x40
	, kSize_0x60
	, kSize_0x80
	, kSize_0x100
	, kSize_0x200
	, kSize_0x300
	, kSize_0x400
	, kSize_0x500
	, kSize_0x600
	, kSize_0x760
	, kSize_0x780
	, kSize_0x7c0
	, kSize_0x7e0
	, kSize_0x800
	, kSize_0xa00
	, kSize_0xa60
	, kSize_0xe00
	, kSize_0xf00
	, kSize_0xf80
	, kSize_0xfe0
	, kSize_0x1000
	, kSize_0x1400
	, kSize_0x1c00
	, kSize_0x1d00
	, kSize_0x1800
	, kSize_0x2000
	, kSize_0x2800
	, kSize_0x3000
	, kSize_0x3c00
	, kSize_0x3e00
	, kSize_0x4000
	, kSize_0x5000
	, kSize_0x6000
	, kSize_0x8000
	, kSize_0xc000
	, kSize_0xbc00
	, kSize_0xdb00
	, kSize_0xdf00
	, kSize_0xe000
	, kSize_0xef00
	, kSize_0xfc00
	, kSize_0x10000
	, kSize_0x16f00
	, kSize_0x18000
	, kSize_0x1cf00
	, kSize_0x1df00
	, kSize_0x20000
	, kSize_0x30000
	, kSize_0x40000
	, kSize_0x1fc00
	, kSize_0x17c00
	, kSize_0x60000
	, kSize_0x80000
	, kSize_Max_
};


// Types of Config masks
enum ConfigMask : uint8_t
{
	kCfgNoMask		// 0xFF
	, kCfg7F		// 0x7F
};

// Types of fuse masks
enum FusesMask : uint8_t
{
	kFuseNoMask		// 0xF
	, kFuse1F		// 0x1F
	, kFuse07		// 0x7
	, kFuse03		// 0x3
	, kFuse01		// 0x1
};

// Presence of Sub-version field on device identification
enum SubversionPresence : uint8_t
{
	kNoSubversion
	, kUseSubversion
};

// Presence of Self field on device identification
enum SelfPresence : uint8_t
{
	kNoSelf
	, kUseSelf
};

// Presence of Revision field on device identification
enum RevisionPresence : uint8_t
{
	kNoRevision
	, kUseRevision
};

// Presence of Config field on device identification
enum ConfigPresence : uint8_t
{
	kNoConfig
	, kUseConfig
};

// Presence of Fab field on device identification
enum FabPresence : uint16_t
{
	kNoFab
	, kUseFab
};

// Presence of Fuse field on device identification
enum FusesPresence : uint16_t
{
	kNoFuses
	, kUseFuses
};

// Maps device to TI User's Guide
enum FamilySLAU : uint8_t
{
	kSLAU012			// SLAU012	(don't care, old parts have no JTAG)
	, kSLAU049			// SLAU049
	, kSLAU056			// SLAU056
	, kSLAU144			// SLAU144
	, kSLAU208			// SLAU208
	, kSLAU259			// SLAU259
	, kSLAU321			// SLAU321	(no Flash memory)
	, kSLAU367			// SLAU367
	, kSLAU378			// SLAU378
	, kSLAU445			// SLAU445
	, kSLAU506			// SLAU506
	, kSlauMax_
};

// Describes a memory block
struct MemoryInfo
{
	// A chained memory info to use as basis (or NULL)
	uint32_t i_refm_ : 8;				// 0
	// Total memory banks
	uint32_t banks_ : 4;
	// Start address or NO_MEM_START
	AddressStart estart_ : 6;
	// Size of block (ignored for NO_MEM_START)
	BlockSize esize_ : 6;
	// Type of memory
	MemoryType type_ : 3;
	// Memory bit alignment
	BitSize bit_size_ : 3;
	// Mapped flag
	uint32_t mapped_ : 1;				// 4
	// Accessible by MPU
	uint32_t access_mpu_ : 1;
	// TYpe of access
	MemAccessType access_type_ : 4;
};

// Describes a memory block and it's class
struct MemoryClasInfo
{
	// Memory class
	MemoryClass class_ : 8;
	// Completes the memory information
	uint32_t i_info_ : 8;
};

// A complete memory layout
struct MemoryLayoutInfo
{
	// Chained memory info to walk before merging with (or 0)
	const MemoryLayoutInfo *ref_;
	// Size of the memory descriptors
	uint32_t entries_;
	// Memory descriptors
	const MemoryClasInfo array_[];
};

// Part name prefix resolver (First byte of name_) and TI SLAU number
struct PrefixResolver
{
	// Chip part number prefix
	const char *prefix;
	// TI User's guide
	FamilySLAU family;
};

// Describes the device or common attributes of a device group
struct Device
{
	// A compressed part number/name (use DecompressChipName())
	const char *name_;					// 0
	// A recursive chain that forms the Memory layout (or NULL)
	const MemoryLayoutInfo *mem_layout_;// 4
	// A base device to copy similarities of (or NULL)
	uint16_t i_refd_ : 10;				// 8
	// Attribute medley contains the Fab attribute
	FabPresence mcu_fab_f : 1;
	// Attribute medley contains the Fuses attribute
	FusesPresence mcu_fuse_f : 1;
	// MCU architecture
	CpuArchitecture arch_ : 2;
	// Type of PSA
	PsaType psa_ : 2;
	// Main ID of the device
	uint16_t mcu_ver_;					// 10: version
	// A attribute medley, depending on the flags below (ordered)
	uint8_t mcu_misc_0;					// 12: a misc of revision, config, fab, self...
	uint8_t mcu_misc_1;					// 15
	uint8_t mcu_misc_2;					// 16
	uint8_t mcu_misc_3;					// 17
	// The fuses mask
	FusesMask mcu_fuse_mask : 3;		// 18
	// Mask to apply to Config
	ConfigMask mcu_cfg_mask : 1;
	// Attribute medley contains a sub-version attribute
	SubversionPresence mcu_sub_f : 1;
	// Attribute medley contains the Self attribute
	SelfPresence mcu_self_f : 1;
	// Attribute medley contains the Rev attribute
	RevisionPresence mcu_rev_f : 1;
	// Attribute medley contains the Config attribute
	ConfigPresence mcu_cfg_f : 1;
};

// Complete list of devices
struct DeviceList
{
	// Total MCU parts
	uint16_t entries_;
	// The list of MCU's
	const uint16_t array_[];
};

#pragma pack()

// A single file should enable this macro to implement the database
#ifdef OPT_IMPLEMENT_DB


// Decompress titles using a char to string map (see NAME_PREFIX_TAB in ExtractChipInfo.py)
static constexpr const PrefixResolver msp430_part_name_prefix[] =
{
	// Ordered from larger string to shorter
	{ "MSP430SL5438A"	, kSLAU208 },
	{ "MSP430FE42"		, kSLAU056 },
	{ "MSP430AFE2"		, kSLAU144 },
	{ "RF430FRL15"		, kSLAU506 },
	{ "MSP430F67"		, kSLAU208 },
	{ "MSP430FG4"		, kSLAU056 },
	{ "MSP430FG6"		, kSLAU208 },
	{ "MSP430FR2"		, kSLAU445 },
	{ "MSP430FR4"		, kSLAU445 },
	{ "MSP430FR5"		, kSLAU367 },
	{ "MSP430FR6"		, kSLAU367 },
	{ "MSP430F1"		, kSLAU049 },
	{ "MSP430F2"		, kSLAU144 },
	{ "MSP430F4"		, kSLAU056 },
	{ "MSP430F5"		, kSLAU208 },
	{ "MSP430F6"		, kSLAU208 },
	{ "MSP430FW"		, kSLAU056 },
	{ "MSP430G2"		, kSLAU144 },
	{ "MSP430C"			, kSLAU321 },
	{ "MSP430L"			, kSLAU321 },
	{ "RF430F5"			, kSLAU378 },
	{ "CC430F"			, kSLAU259 },
	{ "MSP430"			, kSLAU144 },	// the "black sheeps" fits SLAU144
	// All items that the first char of name_ does not fits the range 
	// of 'a' to 'a' + _countof(msp430_part_name_prefix) have integral part names
	// and are of kSLAU144 User's guide family.
};


// Utility to decompress the chip Part number
static void DecompressChipName(char *t, const char *s)
{
	// Check prefix range
	if ( (*s >= 'a') && (*s < ('a' + _countof(msp430_part_name_prefix))) )
	{
		// Locate prefix
		const char *f = msp430_part_name_prefix[*s - 'a'].prefix;
		// Copy prefix...
		while (*f)
			*t++ = *f++;
		// ...and suffix
		++s;
	}
	// Copy string or append suffix
	while (*s)
		*t++ = *s++;
	*t = 0;
}


// Utility to retrieve TI's User's Guide SLAU number
static FamilySLAU MapToChipToSlau(const char *s)
{
	if (*s < 'a' || *s >('a' + _countof(msp430_part_name_prefix)))
		return kSLAU144;
	return msp430_part_name_prefix[*s - 'a'].family;
}

static constexpr uint32_t from_enum_to_address[] =
{
	NO_MEM_START
	, 0x0
	, 0x6
	, 0x20
	, 0x90
	, 0x100
	, 0x200
	, 0xa80
	, 0xb00
	, 0xc00
	, 0xe00
	, 0xf00
	, 0x1000
	, 0x1100
	, 0x1800
	, 0x1900
	, 0x1a00
	, 0x1c00
	, 0x1c80
	, 0x1e00
	, 0x2000
	, 0x2100
	, 0x2380
	, 0x2400
	, 0x2500
	, 0x2c00
	, 0x3100
	, 0x4000
	, 0x4400
	, 0x5c00
	, 0x6000
	, 0x6c00
	, 0x8000
	, 0xa000
	, 0xa400
	, 0xc000
	, 0xc200
	, 0xc400
	, 0xe000
	, 0xe300
	, 0xf000
	, 0xf100
	, 0xf800
	, 0xf840
	, 0xf880
	, 0xfc00
	, 0xfe00
	, 0xffe0
	, 0xc0000
	, 0xf0000
	, 0xf8000
	, 0xfac00
	, 0xffc00
};

static constexpr uint32_t from_block_to_size[] =
{
	0
	, 0x6
	, 0xd
	, 0x10
	, 0x15
	, 0x1a
	, 0x20
	, 0x40
	, 0x60
	, 0x80
	, 0x100
	, 0x200
	, 0x300
	, 0x400
	, 0x500
	, 0x600
	, 0x760
	, 0x780
	, 0x7c0
	, 0x7e0
	, 0x800
	, 0xa00
	, 0xa60
	, 0xe00
	, 0xf00
	, 0xf80
	, 0xfe0
	, 0x1000
	, 0x1400
	, 0x1c00
	, 0x1d00
	, 0x1800
	, 0x2000
	, 0x2800
	, 0x3000
	, 0x3c00
	, 0x3e00
	, 0x4000
	, 0x5000
	, 0x6000
	, 0x8000
	, 0xc000
	, 0xbc00
	, 0xdb00
	, 0xdf00
	, 0xe000
	, 0xef00
	, 0xfc00
	, 0x10000
	, 0x16f00
	, 0x18000
	, 0x1cf00
	, 0x1df00
	, 0x20000
	, 0x30000
	, 0x40000
	, 0x1fc00
	, 0x17c00
	, 0x60000
	, 0x80000
};


""")

def DoHfileStop(fh=sys.stdout):
	fh.write("""
#else	// OPT_IMPLEMENT_DB

extern const DeviceList all_msp430_mcus;

#endif	// OPT_IMPLEMENT_DB

}\t// namespace ChipInfoDB

""")


class Memory(object):
	def __init__(self, node, mems):
		super().__init__()
		if "ref" in node.attrib:
			self.ref = mems.ResolveId(Memory.GetIdent(node.attrib["ref"]))
		else:
			self.ref = None
		self.start = None
		self.size = None
		self.type = None
		self.bits = None
		self.banks = None
		self.mapped = None
		self.access_type = None
		self.access_mpu = None
		for a in node:
			if a.tag == "type":
				self.type = a.text
			elif a.tag == "bits":
				self.bits = a.text
			elif a.tag == "start":
				self.start = a.text
			elif a.tag == "size":
				self.size = a.text
			elif a.tag == "banks":
				self.banks = a.text
			elif a.tag == "mapped":
				self.mapped = a.text
			elif a.tag == "memoryAccess":
				for k in a:
					if k.tag == "type":
						self.access_type = k.text
					elif k.tag == "mpu":
						self.access_mpu = k.text
	def IsPure(self):
		if self.ref is None:
			return False
		return (self.type is None) \
			and (self.bits is None) \
			and (self.start is None) \
			and (self.size is None) \
			and (self.banks is None) \
			and (self.mapped is None) \
			and (self.access_type is None) \
			and (self.access_mpu is None)

	def __eq__(self, value):
		return (self.ref == value.ref) \
			and (self.start == value.start) \
			and (self.size == value.size) \
			and (self.type == value.type) \
			and (self.bits == value.bits) \
			and (self.banks == value.banks) \
			and (self.mapped == value.mapped) \
			and (self.access_type == value.access_type) \
			and (self.access_mpu == value.access_mpu)

	@staticmethod
	def GetIdent(id):
		return "mem_" + mk_identifier(id)

	def DoHfile(self, fh, i_ref, ref_name):
		fh.write("\t\t" + str(i_ref))
		if ref_name:
			fh.write("\t\t\t\t// " + ref_name)
		fh.write("\n")
		#
		if self.banks:
			fh.write("\t\t, " + self.banks + "\n")
		else:
			fh.write("\t\t, 0\n")
		#
		if self.start:
			tmp = int(self.start, 0)
			fh.write("\t\t, kStart_" + hex(tmp) + "\n")
		else:
			fh.write("\t\t, kStart_None\n")
		if self.size:
			tmp = int(self.size, 0)
			fh.write("\t\t, kSize_" + hex(tmp) + "\n")
		else:
			fh.write("\t\t, kSize_None\n")
		if self.type:
			fh.write("\t\t, k" + self.type + "\n")
		else:
			fh.write("\t\t, kNullMemType\n")
		if self.bits:
			fh.write("\t\t, k" + self.bits + "\n")
		else:
			fh.write("\t\t, kNullBitSize\n")
		if self.mapped:
			fh.write("\t\t, " + self.mapped + "\n")
		else:
			fh.write("\t\t, 0\n")
		if self.access_mpu:
			fh.write("\t\t, " + self.access_mpu + "\n")
		else:
			fh.write("\t\t, 0\n")
		if self.access_type:
			fh.write("\t\t, k" + self.access_type + "\n")
		else:
			fh.write("\t\t, kNullMemAccess\n")


class Memories(object):
	def __init__(self, root):
		super().__init__()
		self.Mems = {}
		self.Phys = []
		self.Alias = {}
		self.AddNode(root)

	def AddNode(self, node):
		for child in node:
			if child.tag == 'memory':
				id = Memory.GetIdent(child.attrib["id"])
				m = Memory(child, self)
				self.AddItem(id, m)

	def AddItem(self, id, m):
		for k in self.Mems:
			if m == self.Mems[k]:
				self.Alias[id] = k
				return k
		self.Phys.append(id)
		self.Mems[id] = m
		return id

	def ResolveId(self, id):
		if id in self.Alias:
			return self.Alias[id]
		return id

	def ToIdx(self, ref):
		for i, n in enumerate(self.Phys):
			if n == ref:
				return i
		raise Exception("Internal error when searching key: " + ref)

	def DoHfile(self, fh=sys.stdout):
		fh.write("static constexpr const MemoryInfo all_mem_infos[] =\n{\n")
		for n in self.Phys:
			o = self.Mems[n]
			fh.write("\t{\t// " + n + "\n")
			if o.ref:
				o.DoHfile(fh, self.ToIdx(o.ref) + 1, o.ref)
			else:
				o.DoHfile(fh, 0, None)
			fh.write("\t},\n")
		fh.write("};\n")


class MemoryLayout(object):
	def __init__(self, node, lid, lays, mems):
		super().__init__()
		self.ref = None
		if "ref" in node.attrib:
			self.ref = lays.ResolveId(MemoryLayout.GetIdent(node.attrib["ref"]))
		self.Mems = []
		for child in node:
			if child.tag == 'memory':
				clas = child.attrib["name"]
				mid = Memory.GetIdent(lid + '_' + clas)
				o = Memory(child, mems);
				if o.IsPure():
					self.Mems.append([clas, o.ref]);
				else:
					mid = mems.AddItem(mid, o)
					self.Mems.append([clas, mid]);
			else:
				raise Exception("Unexpected tag: " + child.tag)

	def __eq__(self, value):
		return (self.ref == value.ref) \
			and (self.Mems == value.Mems)

	@staticmethod
	def GetIdent(id):
		return "lyt_" + mk_identifier(id)

	def DoHfile(self, fh, mems):
		if self.ref:
			fh.write("\t&" + self.ref + "\n")
		else:
			fh.write("\tNULL\n")
		fh.write("\t, " + str(len(self.Mems)) + "\n\t, {\n")
		for i in self.Mems:
			tmp = mems.ToIdx(i[1])
			fh.write("\t\t{{kClas{}, {}}},\n".format(i[0], tmp))
		fh.write("\t}\n")

class MemoryLayouts(object):
	def __init__(self, root, mems):
		super().__init__()
		self.Layouts = {}
		self.Alias = {}
		self.Phys = []
		self.AddNode(root, mems)

	def AddNode(self, node, mems):
		for child in node:
			if child.tag == 'memoryLayout':
				lid = MemoryLayout.GetIdent(child.attrib["id"])
				l = MemoryLayout(child, lid, self, mems)
				self.AddItem(lid, l)

	def AddItem(self, lid, l):
		for k in self.Layouts:
			if l == self.Layouts[k]:
				self.Alias[lid] = k
				return k
		self.Phys.append(lid);
		self.Layouts[lid] = l
		return lid

	def ResolveId(self, id):
		if id in self.Alias:
			return self.Alias[id]
		return id

	def AppendDeviceLayout(self, node, mems, id):
		found = None
		for child in node:
			if child.tag == 'memoryLayout':
				if found:
					raise Exception("Duplicate memory layout for " + id)
				if "id" in child.attrib:
					lid = MemoryLayout.GetIdent(node.attrib["id"])
				elif id:
					lid = MemoryLayout.GetIdent(id)
				else:
					raise Exception("Unable to determine an id for element")
				m = MemoryLayout(child, lid, self, mems)
				found = self.AddItem(lid, m);
		return found

	def DoHfile(self, fh, mems):
		for n in self.Layouts:
			o = self.Layouts[n]
			fh.write("static constexpr const MemoryLayoutInfo " + n + " =\n{\n")
			o.DoHfile(fh, mems)
			fh.write("\n};\n")

class Device(object):
	def __init__(self, node, devs, lays, mems):
		super().__init__()
		self.ref = None
		self.name = None
		self.id = None
		self.version = None
		self.subversion = None
		self.revision = None
		self.config = None
		self.self_ = None
		self.fab = None
		self.fuses = None
		self.mconfig = None
		self.mfuses = None
		self.psa = None
		self.bits = None
		self.arch = None
		self.lay = None
		if "id" in node.attrib:
			self.id = "mcu_" + mk_identifier(node.attrib["id"])
		if "ref" in node.attrib:
			self.ref = "mcu_" + mk_identifier(node.attrib["ref"])
		scan_mem_layout = False
		for child in node:
			if child.tag == "description":
				self.name = child.text
			elif child.tag == "idCode":
				for v in child:
					if v.tag == "version":
						self.version = v.text
					elif v.tag == "subversion":
						self.subversion = v.text
					elif v.tag == "revision":
						self.revision = v.text
					elif v.tag == "config":
						self.config = v.text
					elif v.tag == "self":
						self.self_ = v.text
					elif v.tag == "fab":
						self.fab = v.text
					elif v.tag == "fuses":
						self.fuses = v.text
					elif v.tag in ("activationKey", "maxRevision"):
						pass
					else:
						raise Exception("Unexpected identification field " + v.tag + " in " + str(self.id))
			elif child.tag == "idMask":
				for v in child:
					if v.tag == "version":
						if int(v.text, 0) != 0xFFFF:
							raise Exception("Version mask support limited to 0xFFFF for current tool (" + v.tag + "/" + str(self.id) + ")")
					elif v.tag == "subversion":
						if int(v.text, 0) != 0xFFFF:
							raise Exception("Subversion mask support limited to 0xFFFF for current tool (" + v.tag + "/" + str(self.id) + ")")
					elif v.tag == "revision":
						if int(v.text, 0) != 0xFF:
							raise Exception("Revision mask support limited to 0xFF for current tool (" + v.tag + "/" + str(self.id) + ")")
					elif v.tag == "config":
						tmp = int(v.text, 0)
						if tmp not in (0x7F,0xFF):
							raise Exception("Config mask support limited to 0x7f or 0xFF values for current tool (" + v.tag + "/" + str(self.id) + ")")
						self.mconfig = v.text
					elif v.tag == "self":
						if int(v.text, 0) != 0xFFFF:
							raise Exception("Self mask support limited to 0xFFFF for current tool (" + v.tag + "/" + str(self.id) + ")")
					elif v.tag == "fab":
						if int(v.text, 0) != 0xFF:
							raise Exception("Fab mask support limited to 0xFF for current tool (" + v.tag + "/" + str(self.id) + ")")
					elif v.tag == "fuses":
						self.mfuses = v.text
					elif v.tag in ("activationKey", "maxRevision"):
						pass
					else:
						raise Exception("Unexpected identification field " + v.tag + " in " + str(self.id))
			elif child.tag == "psa":
				self.psa = child.text
			elif child.tag == "bits":
				self.bits = child.text
			elif child.tag == "architecture":
				self.arch = child.text
			elif child.tag == "memoryLayout":
				scan_mem_layout = True
		# Resolve empty ID here; use name but this could clash
		if self.id is None:
			if self.name:
				self.id = self.ResolveClashId("mcu_" + mk_identifier(self.name), devs)
			else:
				self.id = self.ResolveClashIdByRef(devs)
		# mem layout gets scanned only by fully resolved childs
		if scan_mem_layout:
			self.lay = lays.AppendDeviceLayout(node, mems, self.id)
		#print(self.id, self.name)

	def ResolveClashId(self, base_id, devs):
		for ch in "!abcdefghijklmnopqrstuvwxyz":
			if ch != '!':
				id = base_id + '_' + ch
			else:
				id = base_id
			colision = False
			for d in devs:
				if d.id == id:
					colision = True
					break
			if not colision:
				return id
		raise Exception("cannot solve id in node " + self.name)

	def ResolveClashIdByRef(self, devs):
		# A reference is required if no id/name was provided
		if self.ref is None:
			raise Exception("cannot solve id in node " + self.name)
		refd = None
		for d in devs:
			if d.id == self.ref:
				refd = d
				break
		if not refd:
			raise Exception("cannot locate reference '{}' for '{}'".format(self.ref, self.name))
		return self.ResolveClashId(refd.id, devs)

	def __lt__(self, value):
		if self.name:
			if value.name:
				return self.name < value.name
			else:
				return False
		elif value.name:
			return True
		else:
			return self.id < value.id

	@staticmethod
	def put_mask_(fh, val, map):
		if val is not None:
			val = int(val, 0)
			if val not in map:
				fh.write("\t\t, " + hex(val) + "\n")	# usually produces a compiler error in C++
			else:
				fh.write("\t\t, " + map[val] + "\n")
		else:
			fh.write("\t\t, " + map[0] + "\n")
	@staticmethod
	def put_bool_mask_(fh, val, map):
		if val is not None:
			s = ", " + map[1]
			tabs = 6 - (len(s) // 4)
			if tabs <= 0:
				tabs = 1
			fh.write("\t\t" + s + '\t'*tabs + "// " + val + "\n")
		else:
			fh.write("\t\t, " + map[0] + "\n")

	def DoHfile(self, fh, devs):
		compress = 0
		MAP_CONFIG = \
		{
			0 : "kCfgNoMask",
			0xFF : "kCfgNoMask",
			0x7F : "kCfg7F",
		}
		MAP_FUSES = \
		{
			0 : "kFuseNoMask",
			0x1 : "kFuse01",
			0x3 : "kFuse03",
			0x7 : "kFuse07",
			0xF : "kFuseNoMask",
			0x1F : "kFuse1F",
		}
		MAP_SUBVERSION_PRES = \
		{
			0 : "kNoSubversion",
			1 : "kUseSubversion",
		}
		MAP_SELF_PRES = \
		{
			0 : "kNoSelf",
			1 : "kUseSelf",
		}
		MAP_REVISION_PRES = \
		{
			0 : "kNoRevision",
			1 : "kUseRevision",
		}
		MAP_CONFIG_PRES = \
		{
			0 : "kNoConfig",
			1 : "kUseConfig",
		}
		MAP_FAB_PRES = \
		{
			0 : "kNoFab",
			1 : "kUseFab",
		}
		MAP_FUSES_PRES = \
		{
			0 : "kNoFuses",
			1 : "kUseFuses",
		}
		cfg_cnt = 0
		fh.write("\t// {}: Part number: {} \n".format(self.id, self.name))
		fh.write("\t{\n")
		if self.name:
			cn = ChipNameCompress(self.name)
			compress = len(self.name) - len(cn)
			fh.write("\t\t\"" + cn + "\"\n")
		else:
			fh.write("\t\tNULL\n")
		if self.lay:
			fh.write("\t\t, &" + self.lay + "\n")
		else:
			fh.write("\t\t, NULL\n")
		#
		if self.ref:
			fh.write("\t\t, {}\n".format(devs.IndexOf(self.ref) + 1))
		else:
			fh.write("\t\t, 0\n")
		#
		self.put_bool_mask_(fh, self.fab, MAP_FAB_PRES)
		self.put_bool_mask_(fh, self.fuses, MAP_FUSES_PRES)
		#
		if self.arch:
			fh.write("\t\t, k" + self.arch + "\n")
		else:
			fh.write("\t\t, kNullArchitecture\n")
		#
		if self.psa:
			fh.write("\t\t, k" + self.psa + "\n")
		else:
			fh.write("\t\t, kNullPsaType\n")
		#
		if self.version is not None:
			fh.write("\t\t, " + self.version + "\n")
		else:
			fh.write("\t\t, NO_MCU_ID0\n")
		#
		if self.subversion is not None:
			fh.write("\t\t, " + extract_lo(self.subversion) + "\n")
			fh.write("\t\t, " + extract_hi(self.subversion) + "\n")
			cfg_cnt += 2
		if self.self_ is not None:
			fh.write("\t\t, " + extract_lo(self.self_) + "\n")
			fh.write("\t\t, " + extract_hi(self.self_) + "\n")
			cfg_cnt += 2
		if self.revision is not None:
			fh.write("\t\t, " + self.revision + "\n")
			cfg_cnt += 1
		if self.config is not None:
			fh.write("\t\t, " + self.config + "\n")
			cfg_cnt += 1
		if self.fab is not None:
			fh.write("\t\t, " + self.fab + "\n")
			cfg_cnt += 1
		if self.fuses is not None:
			fh.write("\t\t, " + self.fuses + "\n")
			cfg_cnt += 1
		if cfg_cnt > 4:
			raise Exception("Too many identification bytes for " + self.id)
		while cfg_cnt < 4:
			fh.write("\t\t, EMPTY_INFO_SLOT\n")
			cfg_cnt += 1
		#
		self.put_mask_(fh, self.mfuses, MAP_FUSES)
		self.put_mask_(fh, self.mconfig, MAP_CONFIG)
		#
		self.put_bool_mask_(fh, self.subversion, MAP_SUBVERSION_PRES)
		self.put_bool_mask_(fh, self.self_, MAP_SELF_PRES)
		self.put_bool_mask_(fh, self.revision, MAP_REVISION_PRES)
		self.put_bool_mask_(fh, self.config, MAP_CONFIG_PRES)
		#
		fh.write("\t},\n")
		return compress


class DeviceList (object):
	def __init__(self, root, lays, mems):
		super().__init__()
		self.Devs = []
		self.AddNode(root, lays, mems)

	def AddNode(self, node, lays, mems):
		for child in node:
			if child.tag == 'device':
				d = Device(child, self.Devs, lays, mems);
				if d.id is None:
					raise Exception("Failed to resolve id for node " + d.name)
				self.Devs.append(d)

	def DoHfile(self, fh=sys.stdout):
		compress = 0
		cnt = 0
		fh.write("static constexpr const Device msp430_mcus_set[] =\n{\n");
		for n in self.Devs:
			compress += n.DoHfile(fh, self)
			if n.name:
				cnt += 1
		fh.write("};\n");
		devs = copy.copy(self.Devs)
		devs.sort()
		print ("Compressed", compress, "bytes from part names")
		fh.write("\n// Supported MCU Table\n");
		fh.write("constexpr const DeviceList all_msp430_mcus =\n{\n");
		fh.write("\t" + str(cnt) + "\n")
		for n in devs:
			if n.name:
				tmp = str(self.IndexOf(n.id))
				if len(tmp) == 1:
					tmp += '\t'
				fh.write("\t, {}\t// {} {}:{}\n".format(tmp, n.name, n.version, n.revision or n.subversion or n.config or "?"))
		fh.write("};\n\n")

		# reveal indexes for special cases
		fh.write("static constexpr uint32_t mcu_MSP430F5438 = {};\n\n".format(self.IndexOf("mcu_MSP430F5438")))

	def IndexOf(self, id):
		for i, n in enumerate(self.Devs):
			if n.id == id:
				return i
		raise Exception("Failed to find device id: " + id)



defs = ET.parse("../ExtractChipInfo/MSP430-devices/devices/defaults.xml")
o = Memories(defs.getroot())
l = MemoryLayouts(defs.getroot(), o)
d = DeviceList(defs.getroot(), l, o)

for fname in os.listdir("../ExtractChipInfo/MSP430-devices/devices"):
	if fname in ("defaults.xml", "p401x.xml", "legacy.xml"):
		continue
	print(fname)
	xml = ET.parse("../ExtractChipInfo/MSP430-devices/devices/" + fname)
	o.AddNode(xml.getroot())
	l.AddNode(xml.getroot(), o)
	d.AddNode(xml.getroot(), l, o)

print("\nOptimized {} memory records".format(len(o.Alias)))
print("Optimized {} memory layout records".format(len(l.Alias)))

with open("../BMP430/ChipInfoDB.h", 'w') as fh:
	DoHfileStart(fh)
	o.DoHfile(fh)
	l.DoHfile(fh, o)
	d.DoHfile(fh)
	DoHfileStop(fh)


