/**
 * Created by dom on 01.12.2016.
 */
'use strict';   // See note about 'use strict'; below

angular.module('weatherStation', ['angularFlaskServices','AuthenticationService','ngCookies'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider.
             when('/', {
                 templateUrl: '../static/partials/home.html',
                 controller: IndexController
             }).
             when('/login', {
                 templateUrl: '../static/partials/login.html',
                 controller: LoginController
             }).
             when('/history', {
                 templateUrl: '../static/partials/history.html',
                 controller: HistoryController
             }).
             when('/stats', {
                 templateUrl: '../static/partials/stats.html',
                 controller: StatsController
             }).
             when('/about', {
                 templateUrl: '../static/partials/about.html',
                 controller: AboutController
             }).
             when('/console', {
                 templateUrl: '../static/partials/console.html',
                 controller: ConsoleController
             }).
             when('/logout', {
                 templateUrl: '../static/partials/logout.html',
                 controller: LogoutController
             }).
             otherwise({
                 redirectTo: '/'
             });
            $locationProvider.html5Mode(true);
    }]);