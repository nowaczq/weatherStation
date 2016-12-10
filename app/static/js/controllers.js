/**
 * Created by dom on 02.12.2016.
 */
'use strict';

function IndexController($scope,AuthenticationService, $timeout,$rootScope)
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

function StatsController($scope)
{

}

function HistoryController($scope)
{

}

function AboutController($scope)
{

}

function LoginController($scope, $http, AuthenticationService, $location)
{
    var vm = this;

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

function LogoutController($scope)
{

}