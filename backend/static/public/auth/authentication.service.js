'use strict'

angular.module('auth').factory('Authentication', ['$window',
  function ($window) {
    var getUserObject = function() {
      var user = $window.user;
      if (!user || !user.id) {
        return null;
      }

      return $window.user;
    };

    var auth = {
      user: getUserObject()
    };

    return auth;
  }
]);
