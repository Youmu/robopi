/// <reference path="angular.min.js"/>"

var model ={
     name: "RoboPi",
     accel:  "0,0,0",
     gyro: "0,0,0",
     temp: 0,
}

var sensorApp = angular.module("sensorApp", []);

console.log("Started");
sensorApp.controller("SensorCtrl", function($scope, $http){
    loadData($scope, $http);
    $scope.sensor = model;
    $scope.fetchData = function(){loadData($scope, $http)};
    $scope.moveRobot = function(x,y,r){moveRobot($scope, $http, x, y, r)};
});

function loadData($scope, $http) {
    console.log("fetchData");
    $http.get("api/sensor/accelerator/")
    .then(function(data){
        $scope.sensor.accel = data.data;
    });
    $http.get("api/sensor/gyro/")
    .then(function(data){
        $scope.sensor.gyro = data.data;
    });
    $http.get("api/sensor/baro/")
    .then(function(data){
        $scope.sensor.baro = data.data.baro;
    });
    model.temp += 1;
    
}

function moveRobot($scope, $http, x, y, r){
    console.log("Move Robot");
    $http.get(`api/motor/move/?x=${x}&y=${y}&r=${r}`);
}