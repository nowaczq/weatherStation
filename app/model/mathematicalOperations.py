from databaseOperations import DatabaseOperations


class MathematicalOperations():

    def __init__(self):
        pass

    def temperature_average(self,start,stop):
        temp_table = DatabaseOperations().get_raw_historical_temperature(start,stop)
        avg = 0
        n = 0

        for temp in temp_table:
            avg = avg + temp[0]
            n = n + 1

        avg = avg / n
        result_list = []
        result_list.append({"temperature": avg})
        return result_list

    def pressure_average(self,start,stop):
        press_table = DatabaseOperations().get_raw_historical_pressure(start,stop)
        avg = 0
        n = 0

        for press in press_table:
            avg = avg + press[0]
            n = n + 1

        avg = avg / n

        result_list = []
        result_list.append({"pressure" : avg})
        return result_list

    def humidity_average(self,start,stop):
        hum_table = DatabaseOperations().get_historical_humidity(start,stop)
        avg = 0
        n = 0

        for hum in hum_table:
            avg = avg + hum[0]
            n = n + 1

        avg = avg / n
        result_list = []
        result_list.append({"humidity" : avg})
        return result_list

    def temperature_min_max(self,start,stop):
        temp_table = DatabaseOperations().get_raw_historical_temperature(start, stop)
        temp_tab = []

        for temp in temp_table:
            temp_tab.append(temp[0])

        temp_tab.sort()
        min = temp_tab[0]
        max = temp_tab[len(temp_tab)-1]

        result_list = []
        result_list.append({"max" : max, "min" : min})

        return result_list

    def pressure_min_max(self,start,stop):
        press_table = DatabaseOperations().get_raw_historical_pressure(start,stop)
        press_tab = []

        for press in press_table:
            press_tab.append(press[0])

        press_tab.sort()
        min = press_tab[0]
        max = press_tab[len(press_tab)-1]

        result_list = []
        result_list.append({"max" : max, "min" : min})

        return result_list

    def humidity_min_max(self,start,stop):
        hum_table = DatabaseOperations().get_historical_humidity(start,stop)
        hum_tab = []

        for hum in hum_table:
            hum_tab.append(hum[0])

        hum_tab.sort()
        min = hum_tab[0]
        max = hum_tab[len(hum_tab)-1]

        result_list = []
        result_list.append({"max" : max, "min" : min})

        return result_list

    def temperature_median(self,start,stop):
        temp_table = DatabaseOperations().get_raw_historical_temperature(start, stop)
        temp_tab = []

        for temp in temp_table:
            temp_tab.append(temp[0])


        temp_tab.sort()
        if len(temp_tab)%2 == 0:
            med = temp_tab[len(temp_tab) / 2]
        else:
            med = temp_tab[(len(temp_tab) + 1) / 2]

        result_list = []
        result_list.append({"temperature" : med})

        return result_list

    def humidity_median(self, start, stop):
        hum_table = DatabaseOperations().get_historical_humidity(start, stop)
        hum_tab = []

        for hum in hum_table:
            hum_tab.append(hum[0])

        hum_tab.sort()
        if len(hum_tab) % 2 == 0:
            med = hum_tab[len(hum_tab) / 2]
        else:
            med = hum_tab[(len(hum_tab) + 1) / 2]

        result_list = []
        result_list.append({"temperature": med})

        return result_list

    def pressure_median(self, start, stop):
        press_table = DatabaseOperations().get_raw_historical_pressure(start, stop)
        press_tab = []

        for press in press_table:
            press_tab.append(press[0])

        press_tab.sort()
        if len(press_tab) % 2 == 0:
            med = press_tab[len(press_tab) / 2]
        else:
            med = press_tab[(len(press_tab) + 1) / 2]

        result_list = []
        result_list.append({"temperature": med})

        return result_list