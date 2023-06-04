#pragma once

#if OPT_TIMER_DMA_WAVE_GEN


/*!
This was designed for hardware autonomous JTCLK pulse generation
but can be reused to produce any kind of "wave" on a single GPIO port.
The main feature of this implementation is to generate a programmable count of
DMA transfers, limited to 65534 transfers. This is ideal when TIM1 is not
available and to circumvent the 8-bit limitation of the RCR register.

Requirements:
	- Two Timer: a master and a slave timer.
	- Master Timer:
		- Used to generate a base timing that counts slave timer up
		- Each timer beat will issue one DMA transfer on the slave timer
		- This timer does not use DMA or interrupts
	- Slave timer:
		- Requires two channels
		- Requires two independent DMA channel, one for each channel; so choose
		channels without conflicts with other DMA channels used by other peripherals
		- First DMA triggers DMA transfer to the BSRR GPIO port register
		- Second DMA disables the Master Timer at the exact programmed DMA count

Parameters (defined on platform.h file):
	kFreq : the desired frequency for DMA triggers
	kOnBeatDma : DMA issued on every beat generated by master timer
*/
template <
	typename SysClk							///< System clock that drives timers
	, const Timer::Unit kTimMaster			///< Master timer
	, const Timer::Unit kTimSlave			///< Slave timer
	, const uint32_t kFreq					///< Frequency of the wave DMA trigger
	, const Timer::Channel kOnBeatDma		///< Timer channel that controls wave DMA
	, const Timer::Channel kOnStopMasterTimer	///< Timer channel used when desired count reaches
	, const uint16_t kSubDiv = 1			///< Counts up every kSubDiv pulses
>
class TimDmaWav
{
public:
	/// Time Base for the JTCLK generation (2 cycles are needed by timer to trigger an update)
	typedef Timer::InternalClock_Hz<kTimMaster, SysClk, 2*kFreq> MasterClock;
	/// Generates the beat that issues a DMA request
	typedef Timer::Any<MasterClock, Timer::Mode::kUpCounter, 1> BeatTimer;
	/// The clock source for the slave timer (a bridge from master to slave timer)
	typedef Timer::MasterSlaveTimers<kTimMaster, kTimSlave, Timer::MasterMode::kUpdate, Timer::SlaveMode::kMasterIsClock, kSubDiv - 1> Bridge;
	/// Time base is managed by prescaler, so use just one step
	typedef Timer::Any<Bridge, Timer::Mode::kSingleShot, 65535> CounterTimer;
	/// Capture compare channel connected to master clock to generate DMA requests
	typedef Timer::AnyInputChannel<kTimSlave, kOnBeatDma, Timer::InputCapture::kTRC, Timer::CaptureEdge::kFalling> MasterClockCapture;
	/// DMA channel that triggers JTCLK generation
	typedef Dma::AnyChannel
		<
		typename MasterClockCapture::DmaInfo_::Update
		, Dma::Dir::kMemToPerCircular
		, Dma::PtrPolicy::kLongPtrInc
		, Dma::PtrPolicy::kLongPtr
		, Dma::Prio::kMedium
		> DmaClk;
	/// A DMA used to stop counting
	typedef Timer::AnyOutputChannel<
		CounterTimer
		, kOnStopMasterTimer	// channel number to control master timer
		, Timer::OutMode::kFrozen	// no output control
		, Timer::Output::kDisabled	// no positive output
		, Timer::Output::kDisabled	// no negative output
		, false					// no preload
		, true					// fast enable
		> MasterClockStopper;
	/// Yet another DMA...
	typedef Dma::AnyChannel
		<
		typename MasterClockStopper::DmaInfo_::Update
		, Dma::Dir::kMemToPer
		, Dma::PtrPolicy::kLongPtr
		, Dma::PtrPolicy::kLongPtr
		, Dma::Prio::kLow
		> StopTimerDmaCh;

public:
	/// Hardware initialization
	static ALWAYS_INLINE void Init()
	{
		static_assert(kSubDiv >= 1, "A non-zero 16-bit value is required for kSubDiv");
		static_assert(kTimMaster != kTimSlave, "Two distinct timer are needed");
		static_assert(kOnBeatDma != kOnStopMasterTimer, "Two distinct channels are needed");
		static_assert(MasterClockCapture::DmaCh_ != MasterClockStopper::DmaCh_, "Selected channels are sharing the same DMA channel (HW limitation)");
		
		BeatTimer::Init();			// master timer generates time base
		CounterTimer::Init();		// slave timer counts periods while triggering DMA
									// this also binds master and slave through Bridge::Setup()
		MasterClockCapture::Setup();
		MasterClockCapture::EnableDma();
		MasterClockCapture::Enable();
		MasterClockStopper::EnableDma();
		DmaClk::Init();
		StopTimerDmaCh::Init();
		StopTimerDmaCh::SetDestAddress(&BeatTimer::GetDevice()->CR1);
		StopTimerDmaCh::SetSourceAddress(&oldval_);
	}
	/// Beat DMA data table (circular mode)
	static ALWAYS_INLINE void SetTarget(volatile void* periph_addr, const void* src_table, const uint16_t table_cnt)
	{
		DmaClk::SetDestAddress(periph_addr);
		DmaClk::SetSourceAddress(src_table);
		DmaClk::SetTransferCount(table_cnt);
	}
	/// Generates the wave with the given count
	static ALWAYS_INLINE void Run(const uint16_t pulses, const bool start_dma = false)
	{
		// Pulse count limit depends on HW register
		assert(pulses <= 65334);
		StopTimerDmaCh::SetTransferCount(1);
		StopTimerDmaCh::Enable();
		DmaClk::Enable();
		// CCR and one shot limited to pulse count
		MasterClockStopper::SetCompare(pulses);
		// Read timer configuration value before enabling
		oldval_ = BeatTimer::GetDevice()->CR1;
		// Start slave then master
		CounterTimer::StartShot();
		if (start_dma)
			MasterClockCapture::GenerateCompareEvent();
		BeatTimer::CounterStart();
	}
	/// Checks if timer are running
	static ALWAYS_INLINE void IsRunning()
	{
		return BeatTimer::IsTimerEnabled();
	}
	/// Halts CPU until all pulses are generated
	static ALWAYS_INLINE void Wait()
	{
		// Let timer and DMA do pulse autonomously
		BeatTimer::WaitForAutoStop(); // StopTimerDmaCh DMA will disable it
	}
	// Called after Wait() to stop all resources
	static ALWAYS_INLINE void Finalize()
	{
		// Stop slave timer and disables both DMAs
		CounterTimer::CounterStop();
		DmaClk::Disable();
		StopTimerDmaCh::Disable();
	}
	/// Runs and waits until it stops
	static ALWAYS_INLINE void RunEx(const uint16_t pulses, const bool start_dma = false)
	{
		Run(pulses, start_dma);
		Wait();
		Finalize();
	}
protected :
	static inline uint32_t oldval_;
};

#endif // OPT_TIMER_DMA_WAVE_GEN

