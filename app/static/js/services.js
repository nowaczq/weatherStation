/**
 * Created by dom on 02.12.2016.
 */
'use strict';

angular.module('angularFlaskServices', ['ngResource'])

	.factory('Post', function($resource) {

		return $resource('/api/post/:postId', {}, {

			query: {

				method: 'GET',

				params: { postId: '' },

				isArray: true

			}

		});

	});