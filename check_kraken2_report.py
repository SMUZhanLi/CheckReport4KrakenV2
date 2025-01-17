#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import argparse

def check_kraken2_report(reportfile:str, ktaxfile:str, newreportfile:str):
    tax2lev = {}
    with open(ktaxfile, 'r') as file:
        for ktax_line in file.readlines():
            line_split = ktax_line.strip().split("\t")
            lev = line_split[4]
            tax = line_split[8]
            tax2lev[tax] = lev
    newreport = []
    with open(reportfile, 'r') as file:
        for report_line in file.readlines():
            line_split = report_line.strip().split("\t")
            lev = line_split[3].strip()
            if (len(lev) == 0 or lev.isdecimal()):
                tax = line_split[5].strip()
                if tax in tax2lev:
                    newlev = tax2lev[tax]
                else:
                    newlev = '-'
                line_split[3] = newlev
                newreport.append('\t'.join(line_split) + '\n')
            else:
                newreport.append(report_line)
    with open(newreportfile, 'w') as file:
        file.writelines(newreport)
    print("Fixed null taxonomic levels for report of kraken.")
    return(None)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i' ,'--report', dest='report', required=True,
        help='Kraken REPORT file to use for abundance estimation')
    parser.add_argument('-d', '--k2db', dest='k2db', required=True,
        help='Location of Kraken database')
    parser.add_argument('-o', '--output', dest='output', required=True,
        help='Checked Kraken REPORT checked output file')
    args=parser.parse_args()
    check_kraken2_report(reportfile=args.report,
                         ktaxfile=os.path.join(args.k2db, "ktaxonomy.tsv"),
                         newreportfile=args.output)
    return(None)

if __name__ == "__main__":
    main()