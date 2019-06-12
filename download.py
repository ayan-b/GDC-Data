from __future__ import print_function

import time

from xena_gdc_etl import xena_dataset, gdc


GDC_XENA_COHORT = [
    'TCGA-BRCA', #
    'TCGA-LUAD', #
    'TCGA-UCEC', #
    'TCGA-LGG', #
    'TCGA-HNSC', #
    'TCGA-PRAD', #
    'TCGA-LUSC', #
    'TCGA-THCA', #
    'TCGA-SKCM', #
    'TCGA-OV', #
    'TCGA-STAD', #
    'TCGA-COAD', #
    'TCGA-BLCA', #
    'TCGA-GBM', #
    'TCGA-LIHC', #
    'TCGA-KIRC', #
    'TCGA-CESC', #
    'TCGA-KIRP', #
    'TCGA-SARC', #
    'TCGA-ESCA', #
    'TCGA-PAAD', #
    'TCGA-PCPG', #
    'TCGA-READ', #
    'TCGA-TGCT', #
    'TCGA-LAML', #
    'TCGA-THYM', #
    'TCGA-ACC', #
    'TCGA-MESO', #
    'TCGA-UVM', #
    'TCGA-KICH', #
    'TCGA-UCS', #
    'TCGA-CHOL', #
    'TCGA-DLBC', #
]

TARGET_DATA = [
    "TARGET-NBL", #
    "TARGET-AML", #
    "TARGET-WT", #
    "TARGET-OS", #
    "TARGET-ALL-P3", #
    "TARGET-RT", #
    "TARGET-CCSK", #
]

xena_dtypes = [
    'masked_cnv',  # Masked Copy Number Segment 
    'mirna',  # miRNA Expression Quantification
    'muse_snv',  # MuSE Variant Aggregation and Masking
    'mutect2_snv',  # MuTect2 Variant Aggregation and Masking
    'somaticsniper_snv',  # SomaticSniper Variant Aggregation and Masking
    'varscan2_snv',  # VarScan2 Variant Aggregation and Masking
    'htseq_counts',  # HTSeq - Counts
    'htseq_fpkm',   # HTSeq - FPKM
    'htseq_fpkm-uq',  # HTSeq - FPKM-UQ
    'methylation450',  # Illumina Human Methylation 450 
]


projects = "TCGA-BRCA"

# xena_dtypes = ["muse_snv"]

# testing code starts here
for xena_dtype in xena_dtypes:
    dataset = xena_dataset.GDCOmicset(
        projects="TCGA-CHOL",
        root_dir=r".",
        xena_dtype = xena_dtype,
    )
    dataset.download().transform().metadata()
