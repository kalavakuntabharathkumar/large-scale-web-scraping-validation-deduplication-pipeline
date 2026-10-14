import os
import pandas as pd
from datasketch import MinHash, MinHashLSH

def signature(text, n=5):
    m=MinHash(num_perm=128)
    tokens=str(text).lower().split()
    for i in range(max(0,len(tokens)-n+1)):
        m.update(" ".join(tokens[i:i+n]).encode())
    return m

def deduplicate(df, column="name", threshold=0.85):
    lsh=MinHashLSH(threshold=threshold, num_perm=128)
    keep=[]
    dropped=set()
    for idx,value in df[column].items():
        if idx in dropped:
            continue
        matches=lsh.query(signature(value))
        if matches:
            dropped.update(matches)
            continue
        lsh.insert(str(idx), signature(value))
        keep.append(idx)
    return df.loc[keep].reset_index(drop=True)

def validate(df):
    required={"name","url","price"}
    missing=required-set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    out=df.copy()
    out["price"]=pd.to_numeric(out["price"],errors="coerce")
    out["valid"]=out["name"].notna() & out["url"].notna() & out["price"].ge(0)
    return out

if __name__=="__main__":
    path=os.getenv("INPUT_FILE","data/products.csv")
    df=pd.read_csv(path)
    clean=deduplicate(validate(df))
    os.makedirs("data",exist_ok=True)
    clean.to_csv("data/products_clean.csv",index=False)
    print(f"Input={len(df)} Output={len(clean)}")
