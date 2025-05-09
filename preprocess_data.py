import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os

class TBIDataPreprocessor:
    def __init__(self, data_path):
        # Get the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to the data file
        full_data_path = os.path.join(current_dir, data_path)
        print(f"Reading data from: {full_data_path}")
        
        self.data = pd.read_csv(full_data_path)
        self.special_codes = [82, 99, 999]
        
        # Create output directory
        output_dir = os.path.join(current_dir, 'output')
        os.makedirs(output_dir, exist_ok=True)
        print(f"Output will be saved to: {output_dir}")
        
        # Define columns
        self.outcome_columns = [
            'FIMCompD', 'FIMExpressD', 'FIMSocialD', 
            'FIMProbSlvD', 'FIMMemD'
        ]
        
        self.confounder_columns = [
            'Age', 'SexF', 'Height', 'Weight',
            'CC_Hypertension', 'SCI',
            'Has_Private_Insurance', 'Has_Government_Insurance'
        ]
        
        self.treatment_column = 'GCS_Severity'
        
    def clean_outcomes(self):
        """Remove rows with special codes in outcome variables"""
        print("Cleaning outcome variables...")
        for col in self.outcome_columns:
            self.data = self.data[~self.data[col].isin(self.special_codes)]
        return self
    
    def convert_treatment_to_binary(self):
        """Convert GCS severity to binary treatment"""
        print("Converting treatment to binary...")
        self.data['treatment'] = (self.data['GCSTot'] <= 8).astype(int)
        return self
    
    def convert_outcomes_to_binary(self):
        """Convert outcome variables to binary based on median split"""
        print("Converting outcomes to binary...")
        for col in self.outcome_columns:
            median = self.data[col].median()
            self.data[f'{col}_binary'] = (self.data[col] > median).astype(int)
        return self
    
    def handle_confounder_special_codes(self):
        """Handle special codes in confounders by creating indicator variables"""
        print("Handling special codes in confounders...")
        for col in self.confounder_columns:
            if col in self.data.columns:
                # Create indicator for special codes
                self.data[f'{col}_special'] = self.data[col].isin(self.special_codes).astype(int)
                # Replace special codes with median
                median = self.data[~self.data[col].isin(self.special_codes)][col].median()
                self.data[col] = self.data[col].replace(self.special_codes, median)
        return self
    
    def standardize_confounders(self):
        """Standardize confounder variables"""
        print("Standardizing confounders...")
        scaler = StandardScaler()
        for col in self.confounder_columns:
            if col in self.data.columns:
                self.data[f'{col}_std'] = scaler.fit_transform(self.data[[col]])
        return self
    
    def save_processed_data(self, output_path):
        """Save processed data to CSV"""
        print("Saving processed data...")
        self.data.to_csv(output_path, index=False)
        return self
    
    def plot_treatment_balance(self):
        """Plot distribution of confounders by treatment group"""
        print("Generating balance plots...")
        for col in self.confounder_columns:
            if f'{col}_std' in self.data.columns:
                plt.figure(figsize=(10, 6))
                sns.boxplot(x='treatment', y=f'{col}_std', data=self.data)
                plt.title(f'Distribution of {col} by Treatment Group')
                plt.savefig(f'output/severity_control_{col}_distribution.png')
                plt.close()
        return self
    
    def run_all(self, output_path):
        """Run all preprocessing steps"""
        print("\nStarting data preprocessing...")
        self.clean_outcomes()
        self.convert_treatment_to_binary()
        self.convert_outcomes_to_binary()
        self.handle_confounder_special_codes()
        self.standardize_confounders()
        self.plot_treatment_balance()
        self.save_processed_data(output_path)
        return self

if __name__ == "__main__":
    # Initialize preprocessor with the data in current directory
    preprocessor = TBIDataPreprocessor('tbi_dataset_cleaned.csv')
    
    # Run all preprocessing steps
    preprocessor.run_all('severity_control_processed.csv')
    
    # Print summary statistics
    print("\nTreatment Group Sizes:")
    print(preprocessor.data['treatment'].value_counts())
    
    print("\nOutcome Binary Distribution:")
    for col in preprocessor.outcome_columns:
        print(f"\n{col}_binary:")
        print(preprocessor.data[f'{col}_binary'].value_counts()) 