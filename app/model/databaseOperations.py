from app.dao.daoObjects import *
from app.config.databaseConfig import db_session
from datetime import datetime


class DatabaseOperations():

    def __init__(self):
        pass

    def get_historical_values(self,start,stop):

        historical_data = HistoricalValues.query.join(CurrentValues.history).filter(HistoricalValues.date >= start) \
            .filter(HistoricalValues.date <= stop) \
            .values(CurrentValues.temperature, CurrentValues.humidity, CurrentValues.pressure, HistoricalValues.date)

        result_list = []

        for temperature, humidity, pressure, date in historical_data:
            result_list.append(
                {"temperature": temperature, "humidity": humidity, "pressure": pressure / 100, "date": date}
            )

        return result_list

    def get_historical_temperature(self,start,stop):

        historical_temp_data = HistoricalValues.query.join(CurrentValues.history).filter(
            HistoricalValues.date >= start) \
            .filter(HistoricalValues.date <= stop) \
            .values(CurrentValues.temperature, HistoricalValues.date)

        result_list = []

        for temperature, date in historical_temp_data:
            result_list.append(
                {"temperature": temperature, "date": date}
            )

        return result_list

    def get_raw_historical_temperature(self,start,stop):
        return HistoricalValues.query.join(CurrentValues.history).filter(
            HistoricalValues.date >= start) \
            .filter(HistoricalValues.date <= stop) \
            .values(CurrentValues.temperature, HistoricalValues.date)


    def get_historical_humidity(self,start,stop):

        historical_hum_data = HistoricalValues.query.join(CurrentValues.history).filter(
            HistoricalValues.date >= start) \
            .filter(HistoricalValues.date <= stop) \
            .values(CurrentValues.humidity, HistoricalValues.date)

        result_list = []

        for humidity, date in historical_hum_data:
            result_list.append(
                {"humidity": humidity, "date": date}
            )

        return result_list

    def get_raw_historical_humidity(self,start,stop):
        return HistoricalValues.query.join(CurrentValues.history).filter(
            HistoricalValues.date >= start) \
            .filter(HistoricalValues.date <= stop) \
            .values(CurrentValues.humidity, HistoricalValues.date)

    def get_historical_pressure(self,start,stop):

        historical_press_data = HistoricalValues.query.join(CurrentValues.history).filter(
            HistoricalValues.date >= start) \
            .filter(HistoricalValues.date <= stop) \
            .values(CurrentValues.pressure, HistoricalValues.date)

        result_list = []

        for pressure, date in historical_press_data:
            result_list.append(
                {"pressure": pressure / 100, "date": date}
            )

        return result_list


    def get_raw_historical_pressure(self,start,stop):
        return HistoricalValues.query.join(CurrentValues.history).filter(
            HistoricalValues.date >= start) \
            .filter(HistoricalValues.date <= stop) \
            .values(CurrentValues.pressure, HistoricalValues.date)

    def get_current_stats(self):
        result_list = []
        current_stats = CurrentValues.query.join(HistoricalValues.current).with_entities(CurrentValues.temperature,
                                                                                         CurrentValues.humidity,
                                                                                         CurrentValues.pressure,
                                                                                         HistoricalValues.date).order_by(
            CurrentValues.id.desc()).first()

        result_list.append({"temperature": current_stats[0], "humidity": current_stats[1], "pressure": current_stats[2] / 100,
                            "date": current_stats[3]})

        return result_list

    def authenticate_user(self,login,password):
        db_login = User.query.with_entities(User.login).filter_by(login=login).first()
        db_password = User.query.with_entities(User.password).filter_by(login=login).first()
        if login == db_login[0] and password == db_password[0]:
            return True
        else:
            return False

    def set_temperature_stats(self,min,max,average,median,start,stop):
        insert_temperature_stats = TemperatureStats(min,max,average,median)
        db_session.add(insert_temperature_stats)
        db_session.commit()

        id_temperature_stats = TemperatureStats.query.with_entities(TemperatureStats.id).order_by(TemperatureStats.id.desc()).first()
        insert_statistic_values = StatisticValues(start,stop,id_temperature_stats,None,None)
        db_session.add(insert_statistic_values)
        db_session.commit()

    def set_humidity_stats(self,min,max,average,median,start,stop):
        insert_humidity_stats = HumidityStats(min,max,average,median)
        db_session.add(insert_humidity_stats)
        db_session.commit()

        id_humidity_stats = HumidityStats.query.with_entities(HumidityStats.id).order_by(HumidityStats.id.desc()).first()
        insert_statistic_values= StatisticValues(start,stop,None,id_humidity_stats,None)
        db_session.add(insert_statistic_values)
        db_session.commit()

    def set_pressure_stats(self,min,max,average,median,start,stop):
        insert_pressure_stat = PressureStats(min,max,average,median)
        db_session.add(insert_pressure_stat)
        db_session.commit()

        id_pressure_stats = PressureStats.query.with_entities(PressureStats.id).order_by(PressureStats.id.desc()).first()
        insert_statistic_values = StatisticValues(start,stop,None,None,id_pressure_stats)
        db_session.add(insert_statistic_values)
        db_session.commit()


    def set_all_stats(self,minTemp,maxTemp,averageTemp,medTemp,minHum,maxHum,averageHum,medHum,minPress,maxPress,averagePress,medPress,start,stop):
        insert_temperature_stats = TemperatureStats(minTemp, maxTemp, averageTemp, medTemp)
        db_session.add(insert_temperature_stats)
        db_session.commit()

        insert_humidity_stats = HumidityStats(minHum, maxHum, averageHum, medHum)
        db_session.add(insert_humidity_stats)
        db_session.commit()

        insert_pressure_stat = PressureStats(minPress, maxPress, averagePress, medPress)
        db_session.add(insert_pressure_stat)
        db_session.commit()

        id_temperature_stats = TemperatureStats.query.with_entities(TemperatureStats.id).order_by(
            TemperatureStats.id.desc()).first()
        id_humidity_stats = HumidityStats.query.with_entities(HumidityStats.id).order_by(
            HumidityStats.id.desc()).first()
        id_pressure_stats = PressureStats.query.with_entities(PressureStats.id).order_by(
            PressureStats.id.desc()).first()

        insert_statistic_values = StatisticValues(start, stop, id_temperature_stats, id_humidity_stats, id_pressure_stats)
        db_session.add(insert_statistic_values)
        db_session.commit()