from datetime import datetime
from multiprocessing import Pool
from typing import List
import logging

def sum_lists(lists: List[List[int]]) -> List[int]:
    return [sum(lst) for lst in lists]

def process_addition(batchid: str, payload: List[List[int]]) -> dict:
    started_at = datetime.utcnow()
    try:
        with Pool() as pool:
            result = pool.map(sum, payload)
        status = "complete"
    except Exception as e:
        logging.error(f"Error processing addition for batchid {batchid}: {e}")
        result = []
        status = "error"
    completed_at = datetime.utcnow()

    return {
        "batchid": batchid,
        "response": result,
        "status": status,
        "started_at": started_at,
        "completed_at": completed_at
    }
