/**
 * Created by dom on 02.12.2016.
 */
'use strict';

function IndexController(AuthenticationService, $timeout,$rootScope)
{
    (function initController()
        {
            if(AuthenticationService.IsLogged())
            {
                $timeout(function ()
                {
                    $rootScope.isLoggedin = true;
                },100);

            }
            else
            {
                $timeout(function ()
                {
                    $rootScope.isLoggedin = false;
                })
            }
        }
    )();


}

function LineGraph(table,elementID,labelText,colour)
{
    $("#"+elementID).empty();
    console.log('no elo' + elementID);
    Morris.Line
    ({
                  element: elementID,
                  data: table,
                  xkey: 'date',
                  ykeys: 'a',
                  xLabels: 'czas',
                  labels: labelText,
                  parseTime:false,
                  hideHover : 'auto',
                  pointFillColors:['#ffffff'],
                  pointStrokeColors: ['black'],
                  lineColors: [colour]
    });
}


function CurrentController($scope,$http,$timeout,$location)
{
    var curTemp = [];
    var curHum = [];
    var curPress = [];
    var i = 0;

    var cur = function ()
    {
        if ($location.path() === '/current')
        {
            $http.get('/current').success
            (
                function(results)
                {
                    $scope.currentValues = results.result;
                    curTemp[i] = {date : $scope.currentValues[0].date, a : $scope.currentValues[0].temperature};
                    curHum[i] = {date : $scope.currentValues[0].date, a : $scope.currentValues[0].humidity};
                    curPress[i] = {date : $scope.currentValues[0].date, a : $scope.currentValues[0].pressure};
                    console.log(new Date());
                    i += 1;
                    LineGraph(curTemp,'temperature-graph','Temperatura','#337ab7');
                    LineGraph(curHum,'humidity-graph','Wilgotność','#5cb85c');
                    LineGraph(curPress,'pressure-graph','Ciśnienie','#f0ad4e');
                }

            );
            $timeout(cur, 5000);

        }
    };

    if ($location.path() === '/current')
        cur();


}

function MonitorController($scope,$location,$timeout,$http)
{
    var top = function ()
    {
        if ($location.path() === '/monitor')
        {
            $http.get('/monitor').success
            (
                function(results)
                {
                    $scope.topValue = results.result;

                }
            );
            $timeout(top,1000);
        }
    };

    if($location.path() === '/monitor')
        top();
}

function StatsController($scope,$http)
{
    $scope.dateList = {};
    $scope.fullStats = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/fullStats',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.tempAvg = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/tempAvg',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.humAvg = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/humAvg',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.pressAvg = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/pressAvg',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.tempMed = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/tempMed',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.humMed = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/humMed',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.pressMed = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/pressMed',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.pressMinMax = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/pressMinMax',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.humMinMax = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/humMinMax',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.tempMinMax = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/tempMinMax',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.tempFullStats = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/tempFullStats',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.pressFullStats = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/pressFullStats',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
    $scope.humFullStats = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/humFullStats',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
            }).error(function () {
                console.log("false");

        })
    };
}

function HistoryController($scope, $http)
{
    $scope.dateList = {};
    $scope.history = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/history',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
                 $("#bar-example").empty();
            }).error(function () {
                console.log("false");

        })

    };
    $scope.temp = function ()
    {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/tempHistory',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
                var jsonData = results.result;
                var table = new Array(jsonData.length);
                for (var i = 0; i < jsonData.length;i++)
                {
                    table[i] = {date : jsonData[i].date, a : parseFloat(jsonData[i].temperature)};
                }
                LineGraph(table,'bar-example','Temperatura','#337ab7');

            }).error(function () {
                console.log("false");

        })
    };
    $scope.hum = function ()
    {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/humHistory',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
                var jsonData = results.result;
                var table = new Array(jsonData.length);
                for (var i = 0; i < jsonData.length;i++)
                {
                    table[i] = {date : jsonData[i].date, a : parseFloat(jsonData[i].humidity)};
                }
                LineGraph(table,'bar-example','Wilgotność','#5cb85c');
            }).error(function () {
                console.log("false");

        })
    };
    $scope.press = function ()
    {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/pressHistory',{"start" : start, "end" : end})
        .success(function (results) {
                $scope.dateList = {};
                console.log("true");
                $scope.dateList = results.result;
                var jsonData = results.result;
                var table = new Array(jsonData.length);
                for (var i = 0; i < jsonData.length;i++)
                {
                    table[i] = {date : jsonData[i].date, a : parseFloat(jsonData[i].pressure)};
                }
                LineGraph(table,'bar-example','Ciśnienie','#f0ad4e');
            }).error(function () {
                console.log("false");

        })
    }
}

function ConsoleController($scope,$http)
{
    $scope.cmdBody = {};
    $scope.cmd = function ()
    {
        var command = $scope.script;
        console.log($scope.script);
        $http.post('/consoleStuff',{"script" : command})
            .success(function(results){
                $scope.cmdBody = {};
                console.log("true");
                $scope.cmdBody = results.result;
                console.log(results.result);
                }

            ).error(function(){
                console.log("false");
        })

    };
    $scope.cmdHistory = function ()
    {
        $http.get('/commandHistory').success
        (
            function(results)
            {
                $scope.cmdHist = results.result;
            }
        )

    }


}

function AboutController($scope)
{

}

function LoginController($scope, AuthenticationService, $location)
{


    (function initController()
        {
            if(AuthenticationService.IsLogged())
            {
                $location.path('/');
                console.log("IsLogged true");
            }
        }
    )();

    $scope.login = function ()
    {
        AuthenticationService.Login($scope.email, $scope.password, function (response)
        {
                  if(response['result'] == true)
                  {
                      AuthenticationService.SetCredentials($scope.email, $scope.password);
                      $location.path('/');
                  }
                  else
                  {
                      $scope.message = true;
                  }

        });

    };


}

function LogoutController($scope, AuthenticationService, $location, $rootScope)
{
    (function initController() {
            if(!AuthenticationService.IsLogged()) {
                $rootScope.isLoggedin = false;
                $location.path('/');
            }
        })();

    AuthenticationService.ClearCredentials();
    $scope.isLoggedin = false;
    $location.path('/');
}