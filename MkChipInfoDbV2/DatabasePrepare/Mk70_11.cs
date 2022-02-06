using Microsoft.Data.Sqlite;

namespace MkChipInfoDbV2
{
	public partial class DatabasePrepare
	{
		static void Mk70_11(SqliteCommand cmd)
		{
			cmd.CommandText = @"
				UPDATE
					Memories2
				SET 
					MemGroup = '70_11',
					RefTo = '70_0'
				WHERE
					Memories2.MemGroup IS NULL
					AND Memories2.BlockId IN (
						'kBlkPeripheral16bit_1', 
						'kBlkInfo_8'
						)
					AND EXISTS (
						SELECT * 
					FROM 
						Memories2 AS m2 
					WHERE 
						Memories2.PartNumber = m2.PartNumber 
						AND m2.MemGroup = '70_0')
				";
			cmd.ExecuteNonQuery();
		}
	}
}
