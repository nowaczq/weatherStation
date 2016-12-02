/**
 * Created by dom on 01.12.2016.
 */
'use strict';   // See note about 'use strict'; below

var myApp = angular.module('weatherStation', [
 'ngRoute',
]);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/index.html',
             }).
             when('/about', {
                 templateUrl: '../static/partials/about.html',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);
// 'use strict';
//
// var myApp = angular.module('weatherStation', [
//  'ngRoute',
// ]);
//
// myApp.config(['$routeProvider',
//      function($routeProvider) {
//          $routeProvider.
//              when('/', {
//                  templateUrl: '/templates/index.html',
//              }).
//              otherwise({
//                  redirectTo: '/'
//              });
//     }]);
// angular.module('weatherStation',['angularFlaskServices'])
//     .config(['$routeProvider', '$locationProvider'],
//     function ($routeProvider, $locationProvider)
//     {
//         $routeProvider
//             .when('/',{
//                 templateUrl:'weatherStation/templates/index.html',
//                 controller: IndexController
//             })
//             .otherwise({
//                 redirectTo: '/'
//             })
//             ;
//         $locationProvider.html5Mode(true);
//     })
//     .run(['$rootScope', '$location', '$http', '$cookieStore',
//
// 		function run($rootScope) {
//
// 			$rootScope.globals = {
//
//
//
// 			};
//
// 		}])
// ;