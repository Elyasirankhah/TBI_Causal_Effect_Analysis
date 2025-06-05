TBIMS Dataset Initial Cleaning Summary
===========================================

1. Initial Dataset Overview
--------------------------
- Total number of source files: 21 CSV files
- Main data files processed:
  * Form1.csv (19,560 rows × 371 columns)
  * Form2.csv
  * TBIID.csv
  * Form1ICD.csv
  * TBIIDMulti.csv
  * TBIMS_Merged.csv (initial output file)

2. Code Definition Files Analysis
-------------------------------
- Total code definition files: 15 files
- Files by category:
  * Form1 related (3 files):
    - Form1_Codes.csv (2,462 rows × 5 columns)
    - Form1_DD.csv (Data Dictionary)
    - Form1_Variables.csv
  * Form1ICD related (3 files):
    - Form1ICD_Codes.csv (0 rows × 5 columns)
    - Form1ICD_DD.csv (4 rows × 3 columns)
    - Form1ICD_Variables.csv (4 rows × 4 columns)
  * Form2 related (3 files)
  * TBIID related (3 files)
  * TBIIDMulti related (3 files)
 
######### Hint: You can find out more info & explanations about these files in the 'TBIMS_Files_Review'

3. Data Merging Operations
-------------------------
- Performed two-stage merging process:
  a) First Merge: Form1 + Form2
     - Key: 'Mod1Id'
     - Join type: Left join
     - Column suffixes: '_Form1' and '_Form2'
  
  b) Second Merge: (Form1+Form2) + TBIID
     - Composite keys: 'Mod1Id' and 'Mod2Id'
     - Join type: Left join

4. Column Processing and Removal
------------------------------
- Initial column counts:
  * Form1: 371 columns
  * After Form2 merge: Additional columns added
  * After TBIID merge: 687 columns
- Column removal criteria:
  * Removed duplicate columns from merged datasets
  * Replaced suspect codes (e.g., 66, 77, 88, 99, 99999, 8888) with NaN
  * Removed columns where >90% values were placeholder codes like 88888 (e.g., ZIP, death cause)
  * Dropped columns with >60% actual missingness (NaNs)
  * Removed redundant identifier columns
- Total columns dropped due to missingness or invalid content: **333**
- Final dataset dimensions:
  * Rows: 79,604
  * Columns: **352**
  * Total cells: ~28,020,608

5. Data Quality Checks
---------------------
- Implemented checks for suspect codes:
  * Monitored values: 82, 88, 888, 8888, 999, 9999, 99999, 666, 6666, 66
  * Total suspect codes replaced: 
    - Form1.csv → 2,888,860 
    - Form2.csv → 8,250,124 
    - TBIID.csv → 3,038
- Data type consistency:
  * Mixed types detected in columns: 17, 18, 19, 291, 375, 376, 377, 422, 423
- Missing value analysis performed on all datasets, leading to structured removal of weak columns

6. File Structure
----------------
- Data files location: TBIMSPublic.2024-11-01/Data/
- Code definition files location: TBIMSPublic.2024-11-01/Code/

7. Final Dataset Statistics
--------------------------
- Output file: TBIMS_Cleaned_For_Causal.csv
- Dimensions: 79,604 × 352
- Total data points: ~28 million
- File size: ~877KB
- Contains merged data from:
  * Form1 (19,560 rows)
  * Form2
  * TBIID
---------------------------
352 columns in the last dataset are those that can be utilized for the Causal Inference Analysis!
