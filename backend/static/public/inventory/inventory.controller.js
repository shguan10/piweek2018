'use strict'

angular.module('inventory').controller('InventoryController', ['$scope', '$http', 'Authentication', '$window',
  function ($scope, $http, Authentication, $window) {
    $scope.totalNumItems = 0;
    $scope.itemCounts = [];
    $scope.authentication = Authentication;
    
    function toTitleCase(str) {
      return str.replace(/\w\S*/g, function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
      });
    }
    
    function formatDate(date_entered) {
      var date = new Date(date_entered);
      
      var month = '' + (date.getMonth() + 1);
      var day = '' + date.getDate();
      var year = date.getFullYear();

      if (month.length < 2) month = '0' + month;
      if (day.length < 2) day = '0' + day;
      
      var hour = '' + date.getMonth();
      var minute = '' + date.getMinutes();
      var second = '' + date.getSeconds();
      
      if (hour.length < 2) hour = '0' + hour;
      if (minute.length < 2) minute = '0' + minute;
      if (second.length < 2) second = '0' + second;
      
      return [year, month, day].join('-') + ' ' + [hour, minute, second].join(':');
    }
    
    $scope.signout = function() {
      $http.get('/api/signout/').then(function (response) {
        $window.location.reload();
      });
    };
    
    $scope.loadFridge = function() {
      $http.get('/api/fridge').then(function (response) {
        var items = response.data.items;
        $scope.totalNumItems = items.length;
        
        items.map(function (item) {
          var name = toTitleCase(item.name);
          var entered_date = formatDate(item.date_entered);
          
          $scope.itemCounts.push({
            name: name,
            last_date: entered_date
          });
        });
        
        $scope.itemCounts.map(function (elem) {
          var lower = elem.name.toLowerCase();
          if ($scope.data[lower]) {
            var expiry = new Date(elem.last_date).getTime() + $scope.data[lower] * 24 * 3600 * 1000;
            elem.expiry_date = formatDate(expiry);
            if (expiry < (new Date()).getTime()) {
              elem.is_expired = true;
            }
          }
        });
      }).catch(function(err) {
        console.error(err);
      });
    };
    
    $scope.recipes = [];
    $scope.recipeData = '';
    $scope.requestRecipes = function() {
      $http.get('/api/fridge/recipes/').then(function (response) {
        $scope.recipes = response.data.hits;
        $scope.recipeData = JSON.stringify($scope.recipes, null, 2);
        // document.getElementById("json").innerHTML = $scope.recipeData;
      }).catch(function(err) {
        console.error(err);
      });
    };
    
    $scope.loadFridge();
    
    $scope.data = {
      "butter":90,
      "peanut butter":90,
      "margarine":90,
      "buttermilk":14,
      "cheese spread":14,
      "condensed milk":5,
      "cottage cheese":7,
      "cream":4,
      "cream cheese":14,
      "evaporated milk":5,
      "milk":7,
      "hard cheese":180,
      "ice cream and sherbet":0,
      "nonfat dry milk":180,
      "processed cheese":28,
      "pudding":4,
      "sour cream":21,
      "whipped cream":0.1,
      "whipping cream":10,
      "yogurt":7,
      "egg":35,
      "roasts and steak":5,
      "chop":5,
      "ground and stew meat":2,
      "bacon":7,
      "canned ham":270,
      "corned beef":7,
      "ham":7,
      "hotdog":14,
      "sausage":2,
      "smoked breakfast links, pattie":7,
      "organ meat":2,
      "lunch meat":14,
      "turkey":2,
      "ground poultry and giblet":2,
      "duck, goose, game bird":2,
      "chicken":4,
      "cooked poultry casserole":4,
      "cooked poultry with broth or gravy":2,
      "nugget":2,
      "apple":30,
      "apricot":5,
      "avocado":5,
      "banana":5,
      "berry":3,
      "herries":3,
      "cranberry":7,
      "grape":5,
      "guava":2,
      "kiwi":8,
      "lemon":14,
      "lime":14,
      "orange":14,
      "grapefruit":14,
      "mango":4,
      "melon":7,
      "nectarine":5,
      "papaya":4,
      "peach":3,
      "pear":5,
      "pineapple":7,
      "plantain":4,
      "plum":5,
      "rhubarb":7,
      "canned fruit":4
    }
  }
]);
