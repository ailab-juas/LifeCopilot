import logging, json, os
import azure.functions as func
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy
from utilities.helper import LLMHelper


def main():
    logging.info('Requested to start processing all documents received')
    # Set up LLM Helper
    llm_helper = LLMHelper()
    # Get all files from Blob Storage
    files_data = llm_helper.blob_client.get_all_files()
    # # Filter out files that have already been processed
    # files_data = list(filter(lambda x : not x['embeddings_added'], files_data)) if req.params.get('process_all') != 'true' else files_data
    # files_data = list(map(lambda x: {'filename': x['filename']}, files_data))
    # Send a message to the queue for each file
    index = 0
    for fd in files_data:

        file_name = fd['filename']
        # Generate the SAS URL for the file
        file_sas = llm_helper.blob_client.get_blob_sas(file_name)

        # Check the file extension
        if file_name.endswith('.txt'):
            # Add the text to the embeddings
            llm_helper.add_embeddings_lc(file_sas)
        else:
            # Get OCR with Layout API and then add embeddigns
            llm_helper.convert_file_and_add_embeddings(file_sas , file_name)

        llm_helper.blob_client.upsert_blob_metadata(file_name, {'embeddings_added': 'true'})
        index = index +1
        print(f"Processed {index}/{len(files_data)} files")


    print(f"Conversion started successfully for {len(files_data)} documents.")


main()