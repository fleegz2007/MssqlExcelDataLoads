import sqlScripts
import config

def createhdctTable():
    sql_create_ichg_table = "CREATE TABLE " + config.table1 + """ (
                                    PERIOD varchar(MAX),
                                    MID varchar(MAX),
                                    DBA varchar(MAX),
                                    ICHG_CODE varchar(MAX),
                                    CARDTYPE varchar(MAX),
                                    VOLUME float,
                                    RATE float,
                                    PI varchar(MAX), --Is this number a consistent code or does it change? Is it int or decimal?
                                    SURCHARGE_AMT float,
                                    DISCOUNT_TYPE_CODE varchar(MAX),
                                    TRAN_COUNT integer,
                                    ICHG_EXP float,
                                    ASSESS_EXP float,
                                    CHG_TYPE_NUM varchar(MAX),
                                    PAYEE varchar(MAX),
                                    MERCH_BILL float,
                                    DIFF integer, --Need more information on this field
                                    MARKUP_BUY_RT_FEE float,
                                );"""

    # create a database connection
    sql_create_detail_table = "CREATE TABLE  " + config.table2 + """ (
                                    PERIOD varchar(MAX), --Is this in that 202102 format?
                                    SUBCHANNEL varchar(MAX),
                                    SHORT varchar(MAX),
                                    CLIENT_G varchar(MAX), --Need to confirm this is text and not a number
                                    ENTITY varchar(MAX),  
                                    REP_CODE varchar(MAX),
                                    MID varchar(MAX),
                                    DBA varchar(MAX), --Is this number a consistent code or does it change? Is it int or decimal?
                                    SIC varchar(MAX), --Guessing this is text
                                    SIC_CAT varchar(MAX),
                                    KEY_SWIPE varchar(MAX),
                                    TIER varchar(MAX), --Is this float int or text?
                                    STATUS varchar(MAX),
                                    OPENED_DATE datetime,
                                    DISC_RATE float,
                                    DISC_PI float, --Not sure what PI is - Float Int or text
                                    SALE_NO integer, --Need more information on this field
                                    SALE_AMOUNT float, --Diff between sale amount and net vol
                                    CREDIT_NO integer, --Need to ensure this is an integer
                                    CREDIT_AM float, --Need to check if this is a float
                                    NET_VOLUME float,
                                    DISC_REV float,
                                    SURCHARGE_REV float,
                                    DISC_INC float,
                                    ICHG_EXP float,
                                    ASSESS_EXP float,
                                    RISK_SC_RECAP float, --Need more info on this field
                                    PROC_FEES float,
                                    DISC_EXP float,
                                    NET_DISCOUNT float,
                                    AUTH_BC_NO float, 
                                    BC_REV float,
                                    BC_EXP float,
                                    OTHER_TNE_NO float,
                                    TNE_REV float,
                                    TNE_EXP float,
                                    ARU_NO float,
                                    ARU_REV float,
                                    ARU_EXP float,
                                    VOICE_NO float,
                                    VOICE_REV float,
                                    VOICE_EXP float,
                                    VOICE_AVS_NO float,
                                    VOICE_AVS_REV float,
                                    VOICE_AVS_EXP float,
                                    REFERRAL_NO float,
                                    REFERRAL_REV float,
                                    REFERRAL_EXP float,
                                    CHECK_NO float,
                                    CHECK_REV float,
                                    CHECK_EXP float,
                                    PROC_PER_ITEM float,
                                    TOTAL_AUTH_REV float,
                                    TOTAL_AUTH_EXP float,
                                    NET_AUTH_REV float,
                                    DEBIT_NO float,
                                    DEBIT_REV float,
                                    DEBIT_EXP float,
                                    NET_DEBIT float,
                                    MO_REV float,
                                    MO_EXP float,
                                    APP_FEE_REV float,
                                    APP_FEE_EXP float,
                                    OTHER_REV float,
                                    OTHER_EXP float,
                                    MISC_EXP float,
                                    DISC_EASI float,
                                    AMEX_ESA float,
                                    CUST_SERV_EXP float,
                                    BSWD_EXP float,
                                    CHG_BACK_NO float,
                                    CHG_BACK_REV float,
                                    CHG_BACK_EXP float,
                                    TOT_MISC_REV float,
                                    TOT_MISC_EXP float,
                                    NET_MISC float,
                                    GROSS_REV float,
                                    GROSS_EXP float,
                                    AMT_DUE float,
                                    SPREAD_PERC int,
                                    PAYEE varchar(MAX),
                                    AMEX_OPTBLUE_VOL float,
                                    AMEX_OPTBLUE_PROCRATE float,
                                    AMEX_OPTBLUE_COUNT float,
                                    AMEX_OPTBLUE_PROCPI float,
                                    BANKCARD_VOL float,
                                    BANKCARD_PROCRATE float,
                                    BANKCARD_COUNT float,
                                    BANKCARD_PROCPI float,
                                                        );"""

    conn = sqlScripts.create_connection(config.driver, config.server, config.database)
    cur = conn.cursor()
    # create tables
    if conn is not None:
        # create headcount table
        cur.execute(sql_create_ichg_table)
        cur.execute(sql_create_detail_table)
        cur.commit()
        cur.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    createhdctTable()