from pathlib import Path
import pm4py
import pandas as pd


# Get the path of the log file
log_file_path = Path(__file__).parent.parent / "data/original/bank_logs.csv"

# Import the log file
dataframe = pd.read_csv(str(log_file_path), sep=',')
# Case id,Task,Event type,User,Timestamp,Task type,Task name,Task_en
# 173688,A_SUBMITTED,COMPLETE,112.0,2011-10-01 00:38:44,A,submitted,A_submitted
dataframe = pm4py.format_dataframe(dataframe, case_id='Case id', activity_key='Task name', timestamp_key='Timestamp')
log = pm4py.convert_to_event_log(dataframe)
# Discover the DFG
dfg  = pm4py.discover_dfg(log)

# Save the DFG as a PNG file
output_dir = Path(__file__).parent.parent / "output"
output_dir.mkdir(exist_ok=True)  # Create the output directory if it doesn't exist

dfg_file_path = output_dir / "dfg.png"
pm4py.save_vis_dfg(*dfg, file_path=dfg_file_path)