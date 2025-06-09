import pandas as pd
import time
import multiprocessing
import dask.dataframe as dd
import numpy as np

def process_data(df):
    # Add a group column for aggregation
    df["group"] = np.random.randint(0, 1000, size=len(df))
    # Perform groupby aggregation
    result = df.groupby("group")["A"].sum()
    return result

def process_chunk(chunk):
    chunk["group"] = np.random.randint(0, 1000, size=len(chunk))
    result = chunk.groupby("group")["A"].sum()
    return result

if __name__ == "__main__":
    # Create a much larger DataFrame (e.g., 100 million rows)
    N = 100_000_000
    df = pd.DataFrame({
        "A": np.random.randint(0, 100, size=N),
        "B": np.random.randint(0, 100, size=N)
    })

    # Sequential execution (may use a lot of RAM)
    start_time = time.time()
    result_seq = process_data(df.copy())
    end_time = time.time()
    print(f"Sequential Groupby Execution Time: {end_time - start_time:.2f} seconds")

    # Parallel execution using multiprocessing
    start_time = time.time()
    num_partitions = 8
    chunks = np.array_split(df, num_partitions)
    with multiprocessing.Pool(processes=num_partitions) as pool:
        results = pool.map(process_chunk, chunks)
    # Combine groupby results from all chunks
    result_parallel = pd.concat(results).groupby("group").sum()
    end_time = time.time()
    print(f"Parallel Groupby Execution Time with multiprocessing: {end_time - start_time:.2f} seconds")

    # Parallel execution using Dask (out-of-core)
    # Add group column first for consistency
    df["group"] = np.random.randint(0, 1000, size=len(df))
    ddf = dd.from_pandas(df, npartitions=8)
    start_time = time.time()
    result_dask = ddf.groupby("group")["A"].sum().compute()
    end_time = time.time()
    print(f"Dask Groupby Execution Time: {end_time - start_time:.2f} seconds")

    # Compare results

# Sequential Groupby Execution Time: 3.55 seconds
# Parallel Groupby Execution Time with multiprocessing: 4.84 seconds
# Dask Groupby Execution Time: 0.98 seconds