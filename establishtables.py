import sqlScripts
import config

tablename = ''

def createhdctTable():
    sql_create_ichg_table = """CREATE TABLE ICHGRPT (
                                    PERIOD text,
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
    sql_create_detail_table = """CREATE TABLE DETAIL ( --Need the name of this table
                                    PERIOD text, --Is this in that 202102 format?
                                    SUBCHANNEL varchar(MAX),
                                    SHORT varchar(MAX),
                                    CLIENT_G varchar(MAX),
                                    ENTITY varchar(MAX),
                                    REP_CODE varchar(MAX),
                                    MID varchar(MAX),
                                    DBA varchar(MAX), --Is this number a consistent code or does it change? Is it int or decimal?
                                    SIC varchar(MAX),
                                    SIC_CAT varchar(MAX),
                                    KEY_SWIPE varchar(MAX),
                                    TIER integer, --Is this lofat or int?
                                    STATUS varchar(MAX),
                                    OPENED_DATE datetime,
                                    DISC_RATE float,
                                    DISC_PI float,
                                    SALE_NO integer, --Need more information on this field
                                    SALE_AMOUNT float,
                                    NET_VOLUME float,
                                    DISC_INC float,
                                    ICHG_EXP float,
                                    ASSESS_EXP float,
                                    RISK_SC_RECAP float,
                                    PROC_FEES float,
                                    DISC_EXP float,
                                    NET_DISCOUNT float,
                                    AUTH_BC_NUM float,
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
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,
                                    VOICE_EXP float,

                                );"""

    conn = sqlScripts.create_connection(config.driver, config.server, config.database)
    cur = conn.cursor()
    # create tables
    if conn is not None:
        # create headcount table
        cur.execute(sql_create_ichg_table)
        cur.commit()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    createhdctTable()