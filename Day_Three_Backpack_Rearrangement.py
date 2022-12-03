def backpack_rearrangement(backpack):
    backpack_separated = backpack.split("\n")
    priorities = 0
    for backpack in backpack_separated:
        index_to_split = int(len(backpack) / 2)
        compartment_one = backpack[:index_to_split]
        compartment_two = backpack[index_to_split:]

        intersection = set(list(compartment_two)).intersection(list(compartment_one))
        for value in list(intersection):
            priorities += ord(value.lower()) - ord("a") + 1
            if value.isupper():
                priorities += 26
    return priorities



print(backpack_rearrangement("""lflZfgnSnlmmlgGfjGthQPtLNsQhvbHLLpSS
zrCVDVFMJTCTcCJMwCThWbtbpbWpPbtbHPLQssLsHP
rBFcrwFzFwwVDcDrzTzJfnRGjllBdGZnnZfhqmdn
FjpnFRDmbRtnbJrFJmSTsGShWVhGqGVVsmqs
ZwPvNPdzNZwfzBNLdNNNNcLvhnQhqMTVsTGSWSqGqTdVWhMT
vgLZHfvLffNLPbggnrbFpJnCbC
hzJzGjGfqmGtDQtDSvVV
plpcMBNBcCTlTgCMbvtrsSVsVJDJlrwDQr
McHBMMcTTHgJnWqnRqjzZnnRzR
ppvsGZhDGprrSjSllwfZ
TTFMMFJMgMHmHmdqdSvNqlSSSNJv
mgBPHTRWFRVcpvsVttppbv
ZZDssfMDMtqqppZLLJzmzSTwNJplTSgpgm
BdCRRHFRbccWWBvBHCdcJVngNVSvTgVNzgNNVmnz
QHFFrBdcGtqPmmQh
qLvQFRgLSSNgqQvRrqLTQvLttwDBFWDwjwFttDdlBBwBwM
nbsmZnbmHbZVCGPVmHWtwlStBDtwBMtwWHMj
CnCbhGCPpPCSnZmrgRNRqNRrLNgrzh
vgLWWHRNLnWwLggWzwLFFzMmBMRMhMhTbhsmmsbbmQTm
rScpJJDDpjtSDPPPJDpjqPCHBBtlTdblmmlhBsMMmTsbmtsl
GHZHCPprSSwgvWNVwVZv
dMrCMJMqvtdFwcjczjQzThtm
gGbLblLpZlHvllQhlQwcjT
GHRWvPRbPHPRvNGbvdRBqdqBBfRqBqnrfF
VsHcljlbhmHbHHlcjVcVShJSCdJCfMrMMQDfRNFCfMRGfNrQ
tGtvLtpgBTGvDMMRdMMgdCNM
pnGnGqGtvtzTLjWqmSSjHhWhWs
NJTDntDNDVjNnjBfjjjcCZCZcVqCSCLqcSScCc
zvhgRgQvvdllgQbHghlvHrRHSScBCRqqwCLGqSMCZCGGGqMZ
pvvrHzdgvlgzQphQsDFmnsNTTtjfjJJmPB
ScnSZSZZlmjmHjjWHHWZftJVJpppwtVVnLJtnptnwt
CFFlQBbbPQqrBwJrJJrGJD
PgTqRddFzgdRPFFbFgqQFgsSjfHWfSHmSMWcjZlmZmjTZM
lzBRtctbnBRBRBBWnDnDWjlLVvwGMrvwrHHQHGmDvHQvHGrV
FsTgFCTSgsCNspzhCGMfTHQVwVMfMmMmrH
hSdSFgghhqpRbLqjntqnPz
DCDnNGFFDQdQmVDNdFVNFccpJLHWSvPLrvvvPtGGhSttLv
sBgTzzZqrBlfljslWBhvHSvPBhSBJSSL
lRlTgMzlzrwRrnmbCMCFnNVMnc
MJQJMJHBrsdrHwts
dbbSVGgbjVqGTVfqddCTpmWWcprgNgWmcWwWswpN
LPdGGdVGPCVdLBlBMlDRRRMD
vdcwZLTdTFFRDHVgmpppMmqZ
jGPzCnQPjlsDVqDpqDHbgP
BjWJrlGQQzrCzBzlzBCGBznzwNRNcwLJdwTJFTHRSTvtLcNN
ngrgqTjJJZnjFJpnqnnVTLzBbbHbLQdLHLHbrdHdHG
lNcltCCtvftfWssPbMQdMBzhbbcBDLdh
PRtWsQCmWsmSsCNCSvCSWlspwgqjqmqjTpnJZwnZVpFwgq
PjWjGDCjmrmWPNmvWDWFmgCNfVJRLfJRfLDLJQlfHplpRbfR
MtZMtcSbccZshTtQTVVTpzHlLRRQLV
cZhbwMnwqsqnhnqtMBnvNFrnGPNPPmgPGCgW
WBjWjWjqZwQJnJZCZZbf
StHSDRPHHcTrTrJpLCCMbrqnJn
RvTTvGqcqTFvSvSRDHvRjlhgWBWBdhjwjGgNjhlj
FSbCqcFsbCPtrcrqhCScbshMjHDGGWBLHBnjGLPBHGGBGnHj
flQdlsgQgGnQHBHjDn
vllgRZdmvsvpgdwZgzJdwRmprqccSFcSShJbTSttqMCrCCch
GwwgCtvHgwcHVVDqpWdfnqVv
sllBsSNBjSrLfqhLgjfqhL
ZbQbZQzgQQPSblBggNQRHGZHHCmwmHFGGcwtJm
CmGVGBTVTmmTWTNLLCVgCSFvDQppQQDDnDQDJpMggfnQft
RrtdqtldPbHzRbnjRfQZjJfMDnMj
wcwhccqrdrrlFmLGCwCtSwtL
pzZznZphZnpcNWSwGwVVPzrPrG
lgFllLLltgbDsrBCwrjWGmwmtw
MgJbDLlMQRJccchrhc
wbbjzZhdGDwLzZSBWqqHmZgssCWqFtMZ
VRJccfvPlTTlQlHQCWQhMMhCCHqQ
RlVfVJcPTVTfvvvJfNJVlcBjGjwhSLdBNGGnjLLBwzGb
bvpqHMVTTpZnqnWRQQQw
tfhFFdSFggfhbldhhZcnRscRcQmnRs
DPzgFJzFLfFbFSgPFgdPglMHpvBpHTCMGpjvMMpLvvNG
JggGLQgQpLpSPRJgGPSnGlFTDBjjRFvRjtBFjWvFjqRj
cmHhZcMHcWjrTBjrvm
dbHwdNNHhwTNThZHdlwQJJwngpgnJGnSPw
DbZjVfjVLhZDLpWPHpMZPmmGNp
lFcJJGcFqnBFqwJCHHMmNHPsdCNp
BlwccRQtBwBrwLGbGhGggzLgzR
RBhZPjlWqgbNbgGLBr
MzSmSzpFdHwpswzzHnzjnvLCbgtrtLGLbJLLJNtJtbwJ
MsSHdmMdpFfmFjpfcPWRhRVZfWQThZ
mqmssPCFhhsJccVg
FTttfwdjjHznJgfngpnc
dNFTjQNRtRNQldRNrRdHMRrlPZqCGlGBCqqZmmbPqDmDCmGW
ZJVRRZZJRcvmPhCJrvhm
PPWQDTfWbnnstlCGvjGrWMGMvr
TbbwddndsnsfDpwFqZFVHBVPqc
tFmpJmgJJgmFDWgRgFrrlGSltSQvZChMtCMM
TLcZHsjLVNBwGQCCGlsCShvh
nqNdwwccBwVLwjjDznZzppbgzFZfDF
qsTqCCCszjlqTssBShlQSSZFgZZhgB
LDPmVgDDJdLPrPgLgPZSFZQfhQGGBQJcSFJS
mvmVbVvtggVtvgdLVvtmptCsNTtjRnpRTTjpsqCp
BdNPLnmFvLFNgnmBmnFGnwSZZZWwqWgqjwWssTHWSS
bJhMzhbVMbDCcVpZtjHMqTMwtttSjH
hzclfCppVqQfbzQVbpzPQLNFBdrvdNGGBnmrmP
nLVLzBDJCCHqdLncqVJgSsDlGsbssmvvvbvbff
jMNHFWNTZZNwMPrPWrrPMMrrvSllbgsllfgbgvQsvGmglZbv
RjPjrjRPtNrwHhBtncCJtJtL
jbhhjhNjvqNbmjMjqhtCFdmPFdlzJzfFfJQJfR
GBBZWrZWgpSsnSngrrSgHzFzFFdClzfFQFlRZftQPR
TrGTrGWHpHWGHWVWsngprHpLbLLVvcqMcNbVNLhwVNbtNb
sQDvDmDLQFDRsdchzhBczLhhPhVz
MbGGMjjGZSjvfHvHSbfwBqcPnqqcPVhPNnqnzjcn
ZwMMHrWvSHbfJfTrbJwSMMfMsQDtsFRptlpdCRpWmptQDRmC
TwMHdcTznLqzTrHdzzzHTdgMRQWRhJhNjjvgQvQQWNjl
tbfsVbDCVSSDtSPQJWPvRNhQtghN
FVGBpGCVFCbfCbVbZCSHqmwqcqLcdHJGwHqqTd
lTlGfjLGwHNMggscsDRwsC
MrFtrzZZPZrtVQtnrrFdQhhDPDSphgDRhDcsCCgWpW
ZJmJVzVVJFHfGbqJGMLv
zsFZVjzlHPfTzGfLGt
mdrrmdMMcBcmNqNbPqfRDLPWPlqTWD
BNQhmmrBrQghgSmNBQQSmvwssjZZSJHljJFFHZJvZV
rLZCsZdMJfdNCsfZMrLdFmssnwgTRQgBBwgRwcngTNVRVQjV
StqDHlStDPgRTqcwjT
GlDGDhbpHhvSHWlzbWlhpzhJdrFLrCLmvdmFZsmJJjJfdv
pJHJMJsJjSMFdHhszFvMhlmmGNlSmmBGllWmVlwcTw
ZqZRDrZCZDtPDPDrCngrnnPQGVmGHVBWGWtGmWVwVlmTlGNl
ZQPgRqrrQPqLnrLMvLphHdvdjpJddb
NwbBjljFbcjtTcccqW
RHZrPHPpNgZTzTqc
sfrPdmPdpsmPPPrfQPVGlwGVBwbGVnFlNQCG
hQdNTlzhdTvrhdnTBqcWBLsBHgWQgBPg
zwzRDbDfqZBLHDLB
wFbFmjjRzfmjGGMGMfmJwwGCCnvNhpvSCNnrvJvCprnnSp
zshNNJbwGFJfGJzzzNRnHGnCnRHcRPgTmPmn
LMDVtZLStrrZClBrVDllLSBWRPTPPRRPmgWPVmPTPHTWgR
SDSqLMlrtLlLtrBqBdlMZjvffCNzwvhjvvzhdfNhvf
SLQmGBmhLSLQTBGBGwdwpJjwwQjwcVpJZJ
sNrWrWPNbHghrbgnNNzbWbFWdZpMpzVpdMZMzMMVZcwwJdwd
frrPNNWshWhhHDvDGDRSBSRvttqv
FJqpgvhJJRjFjZTqDsMHrzwjsSsSszMrMm
PPPQWGtnbbfBmPsFswwsMrcc
QfBtbldtWQfbWbnfGlFqZppvpFZZLhFlpq
ZqSMZHHCMpHTZTWmFTFZPZQJBgVGVJQvVVSDBvBtcBBG
RNsndwsNjsbsgGCgjQBttcBg
NRszRRNzLNNNwNfhCCrfdmTqFZllFFHFFpWhlTmWpq
llbbzDmSspGRpHpzsldzRRsVtFBBFJMMVVFLTTTMVtLTDM
cqgjqvNgvqCjQZqgGGnhMTnMJVLBLMtFhhVFWB
PfGGvQrPCjvjZgGCCCZZZbSmmmHlRpprlHrHwssSRr
mRmpFpWpfMMgLnmS
CdCsqzdRzqStLjSqfMnL
wQRHdTzCQbzCwsTrZBlFZGpVlpFGQD
qnMTnTVSTPTHTHcMZMvVpmppmFmVzFLLFLlFpG
gBjDsjRRwhDDghthwwWZwLmpmwWWLWLbGZ
NhZtZtBgPTNJJNTS
jLjjmpHvzvZrfzQjmfHHWrfbqblLsSlTsqsgqPJbPqVglb
FBcCwDwtwgcgnCwcGchtJSsRqVRVJPPqDlbSDRPq
MBhthFNtMGCwhcwnpQfWjNrQprpvzpgQ
RfCnWfnhCbwHgWjzBgzB
PsVqDsSTshsgszpsph
DPDvTVtTShhSZhmqSvLlQJFnQJJZnbCnlCCZ
pRRdJngltnwwvTNSWqWffqgBqD
HQGcsdrjzMDDBfGMGG
FLhsdbzCLLHjhntpVnRPRvZV
gZNwQHHNRlGvhvhGRvRb
dpSSBDrzdCfcSzfrzZrfCfMbthWWWPttDthvMFWvvvPj
ZdpBpZCrssBJZfSJBzBdCTcnmQwmnVVlmqTQTTQlHLwNnN
ssCpTttVVVpzZDVvRpCsRtDgWBWBBFBJvvJHMBghGghrMJ
lwLmNNLwSblbmSQLfhJHZgHrHhhJJhHHmW
QLSdbdPqndlNlLdSLNQncpRtRTcRVTPPZRCjVCcc
wzzJclzcTThvWSSCqRlQSsNN
rDpVjpVVDpsQSRDRfQmm
GLbjrLpFbgLVLLgdbjVpchcFZhvBwJvtvtJcZwRB
wPgZgLVMfWVTgmTZZZftJjtfjtJCcdpjdCqc
zGGbQQnQGvBBhGQvvvBBSBvQdhdqqCpdddDmJlCcDjCtJdmJ
HszzHBzQBSmGSwTWgswZPWTVgZ
GDFvzCFdrszSdNJrFfjjfqZjRfsjpqmcwZ
WbbVtVnBPWMgBLMBnQQnBQHcjfjpZRwqcwMfcNTZRqqNmT
WQQnVVPHtggLghWWhHnPVQbvlJhSlrvJDlFGJDdDCzGNFF
dVhTBjBHtTVqWRJZRqhJZQ
brSDTbDfcCwDzfCSbwMQnlqCRJnMgWWnZngM
DFwNSrwNwbDzbFTTFtjmBpVdGpHs
dPQfdfTzDrFDmFDBgBFj
RlJRclcswJRvnwPcpjbjbbCZjFjbBmsbFZ
pqncGlcRJpHGpllGHhvPhRTHrQrttVVfrdQzfrTdftfV
RCzTzRMTfCfRRDzRfhSmZZlCslBbZZBVtZBZsqBL
nvvJPpdcFnPcWnFnVZvBqVlZMbZBNVlV
FpWPMdjdPhSTmwfSjD
NDJjNHLLNWjcLLWCLJLZjLDtRqqtgtMqgtqnRqnSRgggtZ
BwrlfFwmQwhwfPBFhsBdFmbQggCgqQVtbRSqttqMngnp
llPPwsPlGshBJGWJLcHvCzNv
rBvTmwdTSbnrvVWsWVftGfJQGT
gNRLLjlPRWnFVRFDFW
lpCpPNZqZCdvdppnSnBr
ShRdCrJgHClZJtZDGMMz
LvqVVTTNbVPLQNFTnwwMtzFZGDDwmtnM
VLbNvpPvTNVqVbbNpbVPGNLPrRWrcRCWdSrCjWSHcHSdWpCh
tNmZnLSZPFLDnLTmhJMWczQdhmWhWH
bGqbgrpsCsWhcChNQfJz
vwlNbppsRGRRSSSDvjTjLZjZ
zgMZhgfBtftSZQQmLHpSWH
cdqcqnrJVGjjqPVjrPnfpJmsQHQQpsSsbsSDmm
NNnrNqNlrNcPTlBvBvgggfMv
llPrrLHBHCrRRBjrHCjBdrPmvJZzZgZbmgJlZmZhMhhmvh
pNDstVtNtGFNSDFScQtfwzzFJwmJhgqzbMwqZJmh
fpNsptGtQcTsSTccprddCWPrWdTRBMMCMd
TTtDVqTsTcJFgbCqmbCq
NWZQnllzfBFZPBGWQGzFPFRNNgHbHrrwbNrmCbggJRHR
nBZjGFjMQBMPZnjfWjstpcctttvVtcTttMpL
qphVCCwnHqhnRVznFwvLtBTLDTWZtwLWWS
JmdlsdlsjfJfrtjTcvtctDZSSB
rsmfPGbrPbPJfPmrsgMrdJdlFTHhFCqhNqVHnNHHCFznhphG
JsWFMJJzrhSSdFdldmmdmdQc
qLLgCVTgLbBvqsQPVdQGcRRmQmdc
bBCBgCCDbLDqTvqqjpShHfzrzMfjtHHSHsfz
nvFSBFlvvgQFFBzQnlQglmRRzqwsrrMJJMrsMqrfrwzf
CjZNCNhLDNbPZZLZZhwVjpcfrqRhsdJqdsshRTTdqJrJ
jNNDDppjpjDWNVLCVVDpGVVPBFtlSQFWvvQvSSQHSgwQnvtB
WhrQWBRWwhzgmpnSpH
LqMVsJVvFMJLJMsfNjsTJvCgFbSmzgpSHzmngHbGPCbm
jvMjjtqVjTRnwZQwBWwt
jfTWSGSTTWhgcngQfbtJfNzztBQBzz
pVVwsdppRVPLVmPsVVHsjPLPzQdzBzQFzFBNNrJZZQBzbbFF
VmsqHmjHmpvGDSWDvlclSl
PNZfTFSFfTFGCHqqmbFm
WjzRWrjVgnjzplrWWjJVppgGPGsgstmPCCtcmssQqGQt
pzjzJVvnzJjWvpPlnVRVrvnlTDLNNhwfdNZLfMZLwLhTNvTw
QFrQZMFVrVpVszzcNTdMRCCb
SvljGmlvLfwLhLLLHlHdNzsRthhbbRccRCRNbC
LfwlDmlvGBSjjlLLgpPpFJqgQndQgZBJ
RBjPRHdjPfqQcfhcdv
SngFcJZJlcnctSlhhsQvGsDGDsDnfs
pSmFgSWNJFNtStrmNtpCCjPVcbjjHbcWTBHBHL
vGjqCPqNPGFGNftLwmZwfQNTLp
hrdBCSHcCJJcCBShJswmLQpLbbQZTLLJmmZp
BdHHSzrBWdzchzzCcdzHddcDVWFnjPjllGggVlWljPFFFWPM
hBtZZnpbhbPZJbnhDtPnpBtpfjfNNzrrCzjFzFzFTjfjjWzJ
gHllMqRSmqcqMTdggMqHlcFzRrFQWNfvrRvzQrWjWvWf
gwqlgHmmdsgwlwMHZtpsbBbtDBThbBht
CsDLFFLFCvczsCsJrCrJJLRgbQQgmMmPbDDQbPnMgMmg
VlwNBNVhjNVNWBwWjtbRMRZzPmQnfQMPnlZP
VWWSSwGTwtwWWNVwwpqJJrcJGvzqCJCqJF
wLwSSbzwCvddlvvlSj
THnQnnHttcvpQzrZRllZ
sTntBHTnVbPbgzsbgL
FwHgrHvFQQwpHhNhTBLdpNNNLd
fCGqCVtszfSslCSzSGsfCssjNTqLTdmjNLBLdnTTTMTjTg
DccfslfgRSSVVzlcSVtzDRVHwQZFrwwvwFWbbbRRWwrFJb
CwwWwwFNRpFFpZQHtsmfqbQDTQTTqb
VcjzLjGjzGjGjVjLdzqmDqHrsmsqGRrHqGqH
RjdVlgdnljlBnSgPCpNwwMWwMM
tCCtqtbPGzsSQVzQTq
mzMmHMpRsRQTsFFV
DpzDwgdMzMLppNmNpDpfgrbhLcGtPrbtrbrbhnbBcC
BvsQBBBLvDQGjDvSQLTvrHprHlRpVlVllgRbRbHPqq
MMMMCpfJFZZMmCzwpVPCWRtHgqWgqClgtt
FwzmfzhFFdFcpvSDSBDThs
fQrGQbFFFrHHtlHPclzzPLvc
mTnwpNCCqMqjmCThpTpSvvtBczstlLznvsztsPPP
mCpTNhmmpCqCmjmpTjmLCpSJQZVfFVrDVfffFFgfgJQFdbgG
GmWjRBSfttcGfRcSclVVJqsTMllsgJVMVZwV
pPFNpfNCdNzCVMTTNqVssqJN
dzPfHCLLhdjjLGRnmnmr
GPhPfGWgggfslffPsVPGsqJMzLQJtBprwQJJGQwLpQrw
ZNdmvbDDbNvHbmZCcJQwMmzMwWWQrrwttp
bvdDNdnvNbnHDdnDHHRSbnqhqhWfjWFVTVhRVjfjFTfP
hTThfWNCDRfsVCDhpgzgbpPZZwbnZQns
GSjGGcCBGmdjdSlGBcmZwzJzpPpJzwPwQbzgPd
BGmcrcStcMMMmrSLmSMCvFVRFDhfFhhNDWWTqFqTvf
ZmjDTTbmqQCCQQSwvhsL
FGVJPmPmtRVRsCvvRLwwhC
JgdHJgmfbjzTpTMf
fTbsVCsssgLNrfNrgm
zQvzZlRvddvpNLpZrMNNLZ
HLvWFHHlFQvzHnnlnvQqhzWvstBwbGVtstjGqjjwqGGCcwGq
JNpNdzzdJhNnfNGBZLqZqlhvSZSG
QswtcmmwwmTmwwcwZSLlZLDSvSvlBZQD
FsVFBbFgFsPwtVBTwgTPcsmpzdNngfzfpCzJdzCJzNCndn
qcvrLBppgpWWWgLcpzPfhNDqdzqwDDzwhV
MZFjFnHFMHbMntMtnwStfddPhDffDfzDfS
QmnjMZnlHjmnMGFnFlMmjlZWzLgsGgcrspBBLCBcgvgBRC
sdfWHjZfrZrSPMCQ
zqtWRDDDRMbrQJPQ
zwhwzmqwzmFpWzvFqBmFvjNHlHfgVLBgdfVfNVjLsl
lRlBTlvlZfhtbGBWtFBz
cqCNjjqjrNrcNjwDqNPCVrSQStSWshFhtQhbQzGzmFCG
HjPPzMcdNqjcNHMqPjdpgpZflfdgnTfdlvlJ
VpwQJVRtHplnnwtppHhqWBCfVdNNPqPBPWsBDq
jzLZCrvvrZjZvqNffvDNDcWDWd
LTrZZLFZbgTzgjZZjFClJhTHTplQpmnQlpmpQR
JGJnSWLGSpWHVHwGGJHpZdwPdTTPMdTMDdlzccPMPv
gqrrmtbrbgggqgBtqmRSrFgNCzvMDvlMPDdddvzBcPMMMDBd
gjrmRgmtRggFtqjbhgbjrtnJJHWLHQWZZLhZsLLGHhSL
BtTDNggLRPdWQHqggg
wrVpVVlCJVGMMJVdHWSdPSqqRwSQSP
vCVrpvvGjlphBRmZBhmBhBND
lqDcZGcSSqSqbDnccSLJgHgLRfnvvJRLmvWJ
FVCFPChQzVhmsFBgddRgJBfdNfJdfv
FzCpmTQzjQCThppTSttqDccMTDGcDG
QCSGBGCrCsMBTCQwMGSfvvLNNnnVLDlNVNDdVdlr
ZHtPffjWbqgtmnNdvljFnFhdVv
JRWbmgmRJtmJMGGwSBBRRRfQ
LqNrCfCQQhtgnPnc
JWBrWrVlbWgbbtcb
VwvTBprdrVJVNLNMNNqfqpjN
bjVqdHrdqVHPsPNbqHbqNdjFGRwRGlttRtMtRtFFGMLHJw
cfSpZnBZWQBZJlGRJJcwGMGL
WWBhTMgDTZghVjgjssbrbddd"""))