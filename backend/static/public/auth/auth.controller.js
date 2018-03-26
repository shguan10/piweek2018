'use strict'

angular.module('auth').controller('AuthController', ['$scope', 'Authentication', '$http', '$mdToast', '$window',
  function ($scope, Authentication, $http, $mdToast, $window) {
    $scope.authentication = Authentication;
    
    $scope.isSignUpError = false;
    $scope.signUpErrorMessage = '';
    $scope.signUpObject = {};
    
    $scope.isSignInError = false;
    $scope.signInErrorMessage = '';
    $scope.signInObject = {};
    
    $scope.signup = function() {
      $scope.isSignUpError = false;
      $http.post('/api/signup/', $scope.signUpObject).then(function (response) {
        $window.location.reload();
      }, function (response) {
        var errors = response.data.errors;
        var message = "Please check the information you entered and tried again";
        if (errors.password1 || errors.password2) {
          message = "Please ensure that the passwords you entered are strong enough and match";
        } else if (errors.email) {
          message = "Please ensure that you entered a valid email";
        } else if (errors.username) {
          message = "Please try a different username";
        }
      
        $scope.isSignUpError = true;
        $scope.signUpErrorMessage = message;
      });
    };
    
    $scope.signin = function() {
      $scope.isSignInError = false;
      $http.post('/api/signin/', $scope.signInObject).then(function (response) {
        $window.location.reload();
      }, function (response) {
        $scope.isSignInError = true;
        $scope.signInErrorMessage = "Please check the information you entered and tried again";
      });
    };
  }
]);
