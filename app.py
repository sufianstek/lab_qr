import datetime
import time

import os
import json
import gspread
import pprint
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials


#LIVE TEST#
scopes = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
json_creds = os.getenv("GOOGLE_SHEETS_CREDS_JSON")

creds_dict = json.loads(json_creds)
creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
client = gspread.authorize(creds)
#LIVE TEST#


'''

#LOCAL TEST#
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('ucc-pahang.json', scope)
client = gspread.authorize(creds)
#LOCAL TEST#

'''

date_times = (datetime.now() + timedelta(hours=8)).strftime("%d/%m/%Y")

###SUKPA###
spreadsheet_sukpa = client.open_by_url("https://docs.google.com/spreadsheets/d/1ILr17LgncRwNmGYmztu-QFdhp7MtOEm1Nnq2QORI3_I")
sukpa_sh = spreadsheet_sukpa.sheet1

sukpa_input = sukpa_sh.row_values(20)

sukpa_input[0]= date_times


###ILKKM###
spreadsheet_ilkkm = client.open_by_url("https://docs.google.com/spreadsheets/d/17g4wofsHYsuWBTokyY2G0ipkQsQS-eWWidvAbuN8ugM")
ilkkm_sh = spreadsheet_ilkkm.sheet1

ilkkm_input = sukpa_sh.row_values(20)

ilkkm_input[0]= date_times

###UMP###
spreadsheet_ump = client.open_by_url("https://docs.google.com/spreadsheets/d/1XYYkgr7laJCmynqWt9v-Inom6I9RNJPOEvENr88aNdA")
ump_sh = spreadsheet_ump.sheet1

ump_input = ump_sh.row_values(20)

ump_input[0]= date_times


###IKPKT###
spreadsheet_ikpkt = client.open_by_url("https://docs.google.com/spreadsheets/d/1AL7AU2uyf4al1kmnyGTE2fALVf5nAMDg7k0ogAvO0Cw")
ikpkt_sh = spreadsheet_ikpkt.sheet1

ikpkt_input = ikpkt_sh.row_values(20)

ikpkt_input[0]= date_times



###UCC STATISTICS###
spreadsheet_uccstats = client.open_by_url("https://docs.google.com/spreadsheets/d/1qUglpzUaioqgCg_PMunjRIq4r0hu9RdcsVBhFazWhyg")

sukpa_stats_sh = spreadsheet_uccstats.worksheet("sukpa")
ilkkm_stats_sh = spreadsheet_uccstats.worksheet("ilkkm")
ump_stats_sh = spreadsheet_uccstats.worksheet("ump")
ikpkt_stats_sh = spreadsheet_uccstats.worksheet("ikpkt")

sukpa_stats_sh.append_row(sukpa_input)
ilkkm_stats_sh.append_row(ilkkm_input)
ump_stats_sh.append_row(ump_input)
ikpkt_stats_sh.append_row(ikpkt_input)
print('success')



