import os
import subprocess
import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(description='Pg')
    parser.add_argument('--input_file_name', type=str, default='list_of_files_skipped.txt',
                        help='')
    parser.add_argument('--folder_to_read_from', type=str, default='./sstagged_files',
                        help='')
    parser.add_argument('--folder_to_move_files_to', type=str, default='./output_folder',
                        help='')
    print(parser.parse_args())
    return parser

def parse_commandline_args():
    return create_parser().parse_args()


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__=="__main__":
    args = parse_commandline_args()

    # input_file_name="list_of_files_skipped.txt"
    # folder_to_read_from = "./sstagged_files"
    # folder_to_move_files_to = "./output_folder"

    input_file_name = args.input_file_name
    folder_to_read_from = args.folder_to_read_from
    folder_to_move_files_to = args.folder_to_move_files_to

    list_of_skipped_files = []
    with open (input_file_name) as f:
        for index,line in enumerate(f):
            if not (line=="\n"):
                list_of_skipped_files.append(int(line))


    list_of_files_in_input_folder=os.listdir(folder_to_read_from)
    files_moved=0
    for each_pos_file in list_of_files_in_input_folder:
        full_path=os.path.join(folder_to_read_from,each_pos_file)
        each_pos_file_split=each_pos_file.split("_")

        #data_id_predtags=each_pos_file_split[4]
        #data_id_predtags_split=data_id_predtags.split(".")
        data_id=each_pos_file_split[4]

        if int(data_id) in list_of_skipped_files:
            print("found in list")
            print(f"dataid:{data_id}")
            subprocess.call(["cp",full_path,folder_to_move_files_to])
            files_moved=files_moved+1
    print(f"total files moved:{files_moved}")


