from os.path import join


base_dir = '/user/wsolomon'
input_dir = join(base_dir,
                'data/processed/1.4.28-whs2k-df_w2v_7M_CLM_reduced.parquet')
model_file = join(base_dir, 'models/1.4.27-whs2k-model_w2v_7M_CLM')

bad_apps = [
    '13684532', '13442778', '13628414', '13439761',
    '12973760, 12090039', '13847958',
]
query_limit = 5

spark_master ='yarn'
spark_cores_max = '3'
spark_driver_memory ='32g'
spark_executor_cores = '60'
spark_executor_instances = '50'
spark_executor_memory = '32g'
spark_folder = '/usr/hdp/current/spark2-client/'
spark_fraction = 0.1
spark_seed = 1234
spark_log_level = 'ERROR'

