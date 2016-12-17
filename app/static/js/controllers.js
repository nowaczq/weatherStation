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

function CurrentController($scope,$http,$timeout)
{
    var cur = function()
    {
        $scope.currentValues = {};
        $http.get('/current').success
        (
            function (results)
            {
                $scope.currentValues = results.result;

                console.log($scope.currentValues[0]);
            }
        );
        $timeout(cur, 5000);
    };
    cur();



    // setInterval($scope.current = function(){
    //     $http.get('/current');
    //     console.log("no elo");
    // },5000);
        // $http.get('/current').success(
        //     function(results)
        //     {
        //         $scope.stats = results.result;
        //         // setTimeout($scope.current, 5000);
        //     }
        // )
    //}
}

function StatsController($scope)
{

}

function HistoryController($scope, $http)
{
    $scope.history = function () {
        var start =  $scope.startDate;
        var end = $scope.endDate;
        $http.post('/history',{"start" : start, "end" : end})
        .success(function (results) {
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