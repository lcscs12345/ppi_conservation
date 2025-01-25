#!/usr/bin/env python

import pandas as pd
import subprocess,os,io,sys,argparse


def valid_file(param):
    base, ext = os.path.splitext(param)
    if ext.lower() not in ('.pdb', '.cif'):
        raise argparse.ArgumentTypeError('File must have a pdb or cif extension')
    return param
    
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='USalign wrapper')
    parser.add_argument('-i', '--model',
                        type=valid_file,
                        metavar='STR',
                        help='model structure in PDB/CIF format',
                        required='True')
    parser.add_argument('-s', '--samples',
                        type=int,
                        metavar='INT',
                        help='Total number of model samples to test, e.g. 250',
                        required='True')
    parser.add_argument('-r', '--reference',
                        type=valid_file,
                        metavar='STR',
                        help='reference structure in PDB/CIF format',
                        required='True')
    parser.add_argument('-c', '--refchain',
                        metavar='STR',
                        help='The chain ID for reference structure, e.g. A,B',
                        required='True')
    parser.add_argument('-o', '--output',
                        metavar='STR',
                        help='pickle output filename. Default: input file basename')
    parser.add_argument('-m', '--mm',
                        metavar='STR',
                        help='structural alignment method, or -mm in USalign',
                        default='-mm')
    parser.add_argument('-n', '--mmvalue',
                        default='1',
                        metavar='INT',
                        help='mm method value')                
    parser.add_argument('-t', '--ter',
                        default='1',
                        metavar='INT',
                        help='ter method value')
    parser.add_argument('-f', '--outfmt',
                        default='1',
                        metavar='INT',
                        help='USalign output format')

    results = parser.parse_args(args)
    return (results.model, results.samples, results.reference, results.refchain, \
            results.output, results.mm, results.mmvalue, results.ter, results.outfmt)
    
def usalign(m, n, t, f, c, r, s, i):
    # args for structural alignment '-mm','1'
    # args for sequence-structural alignment '-TMscore','7'
    dfs = []
    for x in range(int(s)):
        try:
            p = subprocess.Popen(["USalign",r,i,'-chain1',c,'-model2',str(x),
                                  m,str(n),'-ter',str(t),'-outfmt',str(f)], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, errors = p.communicate()
        
            output = output.split('\n')
            output = pd.DataFrame({'header':[output[0],output[2]],'sequence':[output[1],output[3]],'results':output[4]})
            output[['pair','length','d0','seqID','TM-score']] = output.header.str.split('\t', expand=True)
            output['pair'] = output['pair'].str.replace('>','')
            # output['pair'] = output.pair.str.split('/').apply(lambda x: x[-2])
            output[['Lali','RMSD','seqID_ali']] = output.results.str.split('\t', expand=True)
            output['length'] = output['length'].str.replace('L=','').astype(int)
            output['d0'] = output['d0'].str.replace('d0=','').astype(float)
            output['seqID'] = output['seqID'].str.replace('seqID=','').astype(float)
            output['TM-score'] = output['TM-score'].str.replace('TM-score=','').astype(float)
            output['Lali'] = output['Lali'].str.replace('# Lali=','').astype(int)
            output['RMSD'] = output['RMSD'].str.replace('RMSD=','').astype(float)
            output['seqID_ali'] = output['seqID_ali'].str.replace('seqID_ali=','').astype(float)
            output.drop(['header','results'],axis=1,inplace=True)
            
            df = pd.concat([output.head(1).reset_index(),output.tail(1).reset_index()], axis=1)
            df['pairs'] = df['pair'].values.tolist()
            df['sequences'] = df['sequence'].values.tolist()
            df['lengths'] = df['length'].values.tolist()
            df['d0s'] = df['d0'].values.tolist()
            df['seqIDs'] = df['seqID'].values.tolist()
            df['TM-scores'] = df['TM-score'].values.tolist()
            df.drop(['index','sequence','pair','length','d0','seqID','TM-score','Lali','RMSD','seqID_ali'], axis=1, inplace=True)
            df = pd.concat([df,output.head(1)[['Lali','RMSD','seqID_ali']]], axis=1)
            df['model'] = i
            dfs.append(df)
            
        except IndexError:
            print('Warning: Did you use --samples greater than the total number of model samples?')
            pass
            
    dfs = pd.concat(dfs)
    
    return dfs


def main():
    base,ext = os.path.splitext(i)
    if ext.lower() in ('.pdb', '.cif'):
        data = usalign(m, n, t, f, c, r, s, i)
        if o is None:
            data.to_pickle(base + '.usalign.pkl.gz')
        else:
            data.to_pickle(o)
        
if __name__ == "__main__":
    i,s,r,c,o,m,n,t,f = check_arg(sys.argv[1:])
    main()