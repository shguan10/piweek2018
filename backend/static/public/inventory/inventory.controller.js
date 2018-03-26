'use strict'

angular.module('inventory').controller('InventoryController', ['$scope', '$http', 'Authentication',
  function ($scope, $http, Authentication) {
    $scope.totalNumItems = 0;
    $scope.itemCounts = {};
    $scope.authentication = Authentication;
    
    function toTitleCase(str) {
      return str.replace(/\w\S*/g, function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
      });
    }
    
    $scope.loadFridge = function() {
      $http.get('/api/fridge').then(function (response) {
        var items = response.data.items;
        $scope.totalNumItems = items.length;
        
        items.map(function (item) {
          var name = toTitleCase(item.name);
          if (!$scope.itemCounts[name]) {
            $scope.itemCounts[name] = 1;
          } else {
            $scope.itemCounts[name]++;
          }
        });
      }).catch(function(err) {
        console.error(err);
      });
    };
    
    $scope.loadFridge();
  }
]);
