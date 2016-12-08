/**
 * Created by dom on 01.12.2016.
 */
'use strict';   // See note about 'use strict'; below

angular.module('weatherStation', ['angularFlaskServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider.
             when('/', {
                 templateUrl: '../static/partials/index.html',
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
             otherwise({
                 redirectTo: '/'
             });
            $locationProvider.html5Mode(true);
    }]);