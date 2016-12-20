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
            $http.get('current').success
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

function StatsController($scope)
{

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

    }
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
    }
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
    }
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


function ConsoleController($scope)
{

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