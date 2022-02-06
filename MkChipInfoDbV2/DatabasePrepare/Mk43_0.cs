using Microsoft.Data.Sqlite;

namespace MkChipInfoDbV2
{
	public partial class DatabasePrepare
	{
		static void Mk43_0(SqliteCommand cmd)
		{
			cmd.CommandText = @"
				DROP TABLE IF EXISTS TmpParts;
				CREATE TEMP TABLE TmpParts AS
				SELECT DISTINCT PartNumber
				FROM
					Memories2 AS m1
				WHERE EXISTS (
						SELECT * 
						FROM Memories2 AS m2 
						WHERE m1.PartNumber = m2.PartNumber 
							AND m2.BlockId = 'kBlkBsl_0'
							 AND m2.MemGroup IS NULL
						)
					AND EXISTS (
						SELECT * 
						FROM Memories2 AS m3 
						WHERE m1.PartNumber = m3.PartNumber 
							AND m3.BlockId = 'kBlkInfo_0'
							 AND m3.MemGroup IS NULL
						)
					AND EXISTS (
						SELECT * 
						FROM Memories2 AS m4 
						WHERE m1.PartNumber = m4.PartNumber 
							AND m4.BlockId = 'kBlkPeripheral16bit_0'
						)
					AND EXISTS (
						SELECT * 
						FROM Memories2 AS m5 
						WHERE m1.PartNumber = m5.PartNumber 
							AND m5.BlockId = 'kBlkPeripheral8bit_0'
						)
				";
			cmd.ExecuteNonQuery();
			cmd.CommandText = @"
				UPDATE
					Memories2
				SET 
					MemGroup = '43_0'
				FROM
					TmpParts t1
				WHERE
					Memories2.PartNumber = t1.PartNumber
					AND Memories2.BlockId IN (
						'kBlkBsl_0', 
						'kBlkInfo_0', 
						'kBlkPeripheral16bit_0', 
						'kBlkPeripheral8bit_0',
						-- Overrides
						'kBlkRam_1',
						'kBlkMain_6',
						'kBlkLcd_1'
					)
				";
			cmd.ExecuteNonQuery();
		}
	}
}
