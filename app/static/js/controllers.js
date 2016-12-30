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

function CurrentController($scope,$http,$timeout,$location)
{
    var cur = function ()
    {
        if ($location.path() === '/current')
        {
            $http.get('/current').success
            (
                function(results)
                {
                    $scope.currentValues = results.result;
                    console.log($scope.currentValues[0]);
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