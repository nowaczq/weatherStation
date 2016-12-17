from app import app
import thread

if __name__ == '__main__':
    try:
        from app.job.sensorData import SensorData
        thread.start_new_thread(SensorData().insert_data_to_db_timestamp,(5,))
    except  OSError:
        pass

    app.run(debug=True, host='0.0.0.0')