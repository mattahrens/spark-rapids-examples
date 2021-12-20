#
# Copyright (c) 2019-2021, NVIDIA CORPORATION. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pyspark.sql.types import *

label = 'delinquency_12'

schema = StructType([
    StructField('orig_channel', FloatType()),
    StructField('first_home_buyer', FloatType()),
    StructField('loan_purpose', FloatType()),
    StructField('property_type', FloatType()),
    StructField('occupancy_status', FloatType()),
    StructField('property_state', FloatType()),
    StructField('product_type', FloatType()),
    StructField('relocation_mortgage_indicator', FloatType()),
    StructField('seller_name', FloatType()),
    StructField('mod_flag', FloatType()),
    StructField('orig_interest_rate', FloatType()),
    StructField('orig_upb', IntegerType()),
    StructField('orig_loan_term', IntegerType()),
    StructField('orig_ltv', FloatType()),
    StructField('orig_cltv', FloatType()),
    StructField('num_borrowers', FloatType()),
    StructField('dti', FloatType()),
    StructField('borrower_credit_score', FloatType()),
    StructField('num_units', IntegerType()),
    StructField('zip', IntegerType()),
    StructField('mortgage_insurance_percent', FloatType()),
    StructField('current_loan_delinquency_status', IntegerType()),
    StructField('current_actual_upb', FloatType()),
    StructField('interest_rate', FloatType()),
    StructField('loan_age', FloatType()),
    StructField('msa', FloatType()),
    StructField('non_interest_bearing_upb', FloatType()),
    StructField(label, IntegerType()),
])


name_mapping = {
    'WITMER FUNDING, LLC': 'Witmer',
    'WELLS FARGO CREDIT RISK TRANSFER SECURITIES TRUST 2015': 'Wells Fargo',
    'WELLS FARGO BANK,  NA': 'Wells Fargo',
    'WELLS FARGO BANK, N.A.': 'Wells Fargo',
    'WELLS FARGO BANK, NA': 'Wells Fargo',
    'USAA FEDERAL SAVINGS BANK': 'USAA',
    'UNITED SHORE FINANCIAL SERVICES, LLC D\\/B\\/A UNITED WHOLESALE MORTGAGE': 'United Seq(e',
    'U.S. BANK N.A.': 'US Bank',
    'SUNTRUST MORTGAGE INC.': 'Suntrust',
    'STONEGATE MORTGAGE CORPORATION': 'Stonegate Mortgage',
    'STEARNS LENDING, LLC': 'Stearns Lending',
    'STEARNS LENDING, INC.': 'Stearns Lending',
    'SIERRA PACIFIC MORTGAGE COMPANY, INC.': 'Sierra Pacific Mortgage',
    'REGIONS BANK': 'Regions',
    'RBC MORTGAGE COMPANY': 'RBC',
    'QUICKEN LOANS INC.': 'Quicken Loans',
    'PULTE MORTGAGE, L.L.C.': 'Pulte Mortgage',
    'PROVIDENT FUNDING ASSOCIATES, L.P.': 'Provident Funding',
    'PROSPECT MORTGAGE, LLC': 'Prospect Mortgage',
    'PRINCIPAL RESIDENTIAL MORTGAGE CAPITAL RESOURCES, LLC': 'Principal Residential',
    'PNC BANK, N.A.': 'PNC',
    'PMT CREDIT RISK TRANSFER TRUST 2015-2': 'PennyMac',
    'PHH MORTGAGE CORPORATION': 'PHH Mortgage',
    'PENNYMAC CORP.': 'PennyMac',
    'PACIFIC UNION FINANCIAL, LLC': 'Other',
    'OTHER': 'Other',
    'NYCB MORTGAGE COMPANY, LLC': 'NYCB',
    'NEW YORK COMMUNITY BANK': 'NYCB',
    'NETBANK FUNDING SERVICES': 'Netbank',
    'NATIONSTAR MORTGAGE, LLC': 'Nationstar Mortgage',
    'METLIFE BANK, NA': 'Metlife',
    'LOANDEPOT.COM, LLC': 'LoanDepot.com',
    'J.P. MORGAN MADISON AVENUE SECURITIES TRUST, SERIES 2015-1': 'JP Morgan Chase',
    'J.P. MORGAN MADISON AVENUE SECURITIES TRUST, SERIES 2014-1': 'JP Morgan Chase',
    'JPMORGAN CHASE BANK, NATIONAL ASSOCIATION': 'JP Morgan Chase',
    'JPMORGAN CHASE BANK, NA': 'JP Morgan Chase',
    'JP MORGAN CHASE BANK, NA': 'JP Morgan Chase',
    'IRWIN MORTGAGE, CORPORATION': 'Irwin Mortgage',
    'IMPAC MORTGAGE CORP.': 'Impac Mortgage',
    'HSBC BANK USA, NATIONAL ASSOCIATION': 'HSBC',
    'HOMEWARD RESIDENTIAL, INC.': 'Homeward Mortgage',
    'HOMESTREET BANK': 'Other',
    'HOMEBRIDGE FINANCIAL SERVICES, INC.': 'HomeBridge',
    'HARWOOD STREET FUNDING I, LLC': 'Harwood Mortgage',
    'GUILD MORTGAGE COMPANY': 'Guild Mortgage',
    'GMAC MORTGAGE, LLC (USAA FEDERAL SAVINGS BANK)': 'GMAC',
    'GMAC MORTGAGE, LLC': 'GMAC',
    'GMAC (USAA)': 'GMAC',
    'FREMONT BANK': 'Fremont Bank',
    'FREEDOM MORTGAGE CORP.': 'Freedom Mortgage',
    'FRANKLIN AMERICAN MORTGAGE COMPANY': 'Franklin America',
    'FLEET NATIONAL BANK': 'Fleet National',
    'FLAGSTAR CAPITAL MARKETS CORPORATION': 'Flagstar Bank',
    'FLAGSTAR BANK, FSB': 'Flagstar Bank',
    'FIRST TENNESSEE BANK NATIONAL ASSOCIATION': 'Other',
    'FIFTH THIRD BANK': 'Fifth Third Bank',
    'FEDERAL HOME LOAN BANK OF CHICAGO': 'Fedral Home of Chicago',
    'FDIC, RECEIVER, INDYMAC FEDERAL BANK FSB': 'FDIC',
    'DOWNEY SAVINGS AND LOAN ASSOCIATION, F.A.': 'Downey Mortgage',
    'DITECH FINANCIAL LLC': 'Ditech',
    'CITIMORTGAGE, INC.': 'Citi',
    'CHICAGO MORTGAGE SOLUTIONS DBA INTERFIRST MORTGAGE COMPANY': 'Chicago Mortgage',
    'CHICAGO MORTGAGE SOLUTIONS DBA INTERBANK MORTGAGE COMPANY': 'Chicago Mortgage',
    'CHASE HOME FINANCE, LLC': 'JP Morgan Chase',
    'CHASE HOME FINANCE FRANKLIN AMERICAN MORTGAGE COMPANY': 'JP Morgan Chase',
    'CHASE HOME FINANCE (CIE 1)': 'JP Morgan Chase',
    'CHASE HOME FINANCE': 'JP Morgan Chase',
    'CASHCALL, INC.': 'CashCall',
    'CAPITAL ONE, NATIONAL ASSOCIATION': 'Capital One',
    'CALIBER HOME LOANS, INC.': 'Caliber Funding',
    'BISHOPS GATE RESIDENTIAL MORTGAGE TRUST': 'Bishops Gate Mortgage',
    'BANK OF AMERICA, N.A.': 'Bank of America',
    'AMTRUST BANK': 'AmTrust',
    'AMERISAVE MORTGAGE CORPORATION': 'Amerisave',
    'AMERIHOME MORTGAGE COMPANY, LLC': 'AmeriHome Mortgage',
    'ALLY BANK': 'Ally Bank',
    'ACADEMY MORTGAGE CORPORATION': 'Academy Mortgage',
    'NO CASH-OUT REFINANCE': 'OTHER REFINANCE',
    'REFINANCE - NOT SPECIFIED': 'OTHER REFINANCE',
    'Other REFINANCE': 'OTHER REFINANCE',
}

performance_schema = StructType([
    StructField('loan_id', LongType()),
    StructField('monthly_reporting_period', StringType()),
    StructField('servicer', StringType()),
    StructField('interest_rate', DoubleType()),
    StructField('current_actual_upb', DoubleType()),
    StructField('loan_age', DoubleType()),
    StructField('remaining_months_to_legal_maturity', DoubleType()),
    StructField('adj_remaining_months_to_maturity', DoubleType()),
    StructField('maturity_date', StringType()),
    StructField('msa', DoubleType()),
    StructField('current_loan_delinquency_status', IntegerType()),
    StructField('mod_flag', StringType()),
    StructField('zero_balance_code', StringType()),
    StructField('zero_balance_effective_date', StringType()),
    StructField('last_paid_installment_date', StringType()),
    StructField('foreclosed_after', StringType()),
    StructField('disposition_date', StringType()),
    StructField('foreclosure_costs', DoubleType()),
    StructField('prop_preservation_and_repair_costs', DoubleType()),
    StructField('asset_recovery_costs', DoubleType()),
    StructField('misc_holding_expenses', DoubleType()),
    StructField('holding_taxes', DoubleType()),
    StructField('net_sale_proceeds', DoubleType()),
    StructField('credit_enhancement_proceeds', DoubleType()),
    StructField('repurchase_make_whole_proceeds', StringType()),
    StructField('other_foreclosure_proceeds', DoubleType()),
    StructField('non_interest_bearing_upb', DoubleType()),
    StructField('principal_forgiveness_upb', StringType()),
    StructField('repurchase_make_whole_proceeds_flag', StringType()),
    StructField('foreclosure_principal_write_off_amount', StringType()),
    StructField('servicing_activity_indicator', StringType()),
])

acquisition_schema = StructType([
    StructField('loan_id', LongType()),
    StructField('orig_channel', StringType()),
    StructField('seller_name', StringType()),
    StructField('orig_interest_rate', DoubleType()),
    StructField('orig_upb', IntegerType()),
    StructField('orig_loan_term', IntegerType()),
    StructField('orig_date', StringType()),
    StructField('first_pay_date', StringType()),
    StructField('orig_ltv', DoubleType()),
    StructField('orig_cltv', DoubleType()),
    StructField('num_borrowers', DoubleType()),
    StructField('dti', DoubleType()),
    StructField('borrower_credit_score', DoubleType()),
    StructField('first_home_buyer', StringType()),
    StructField('loan_purpose', StringType()),
    StructField('property_type', StringType()),
    StructField('num_units', IntegerType()),
    StructField('occupancy_status', StringType()),
    StructField('property_state', StringType()),
    StructField('zip', IntegerType()),
    StructField('mortgage_insurance_percent', DoubleType()),
    StructField('product_type', StringType()),
    StructField('coborrow_credit_score', DoubleType()),
    StructField('mortgage_insurance_type', DoubleType()),
    StructField('relocation_mortgage_indicator', StringType()),
])

categorical_columns = [
    'orig_channel',
    'first_home_buyer',
    'loan_purpose',
    'property_type',
    'occupancy_status',
    'property_state',
    'product_type',
    'relocation_mortgage_indicator',
    'seller_name',
    'mod_flag',
]

numeric_columns = [
    'orig_interest_rate',
    'orig_upb',
    'orig_loan_term',
    'orig_ltv',
    'orig_cltv',
    'num_borrowers',
    'dti',
    'borrower_credit_score',
    'num_units',
    'zip',
    'mortgage_insurance_percent',
    'current_loan_delinquency_status',
    'current_actual_upb',
    'interest_rate',
    'loan_age',
    'msa',
    'non_interest_bearing_upb',
    'delinquency_12',
]

default_params = {
    'eta': 0.1,
    'gamma': 0.1,
    'missing': 0.0,
    'maxDepth': 10,
    'maxLeaves': 256,
    'growPolicy': 'depthwise',
    'minChildWeight': 30.0,
    'lambda_': 1.0,
    'scalePosWeight': 2.0,
    'subsample': 1.0,
    'nthread': 1,
    'numRound': 100,
    'numWorkers': 1,
}