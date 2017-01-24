angular.module('todoApp', ['ngCookies'])
  .controller('TodoListController', function($scope, $http, $cookies) {
  window.x = $scope;
    var todoList = this;
    $scope.todos = [];
       var todo_token = $cookies.get('todo_token') ? $cookies.get('todo_token') : '';
       $scope.loading = true;

       $http({
        method: 'GET',
        url: '/api/all/',
        headers:{'Content-Type':'application/json',
                'token': todo_token},
      }).then(function(response) {
        $scope.todos = response.data.data;
        $cookies.put('todo_token', response.data.token);
        $scope.loading = false;
      });

    todoList.addTodo = function() {
    $http({
        method:'POST',
        url: '/api/task/',
        headers: {'Content-Type':'application/json','token': todo_token},
        data: {activity: todoList.todoText, status: false, is_archived: false,},
        }).then(function(response) {
        $scope.todos = response.data.data;
        $cookies.put('todo_token', response.data.token);
        $scope.loading = false;
    })
      //todoList.todos.push({text:todoList.todoText, done:false});
      todoList.todoText = '';
    };

    todoList.remaining = function() {
      var count = 0;
      angular.forEach(todoList.todos, function(todo) {
        count += todo.status ? 0 : 1;
      });
      return count;
    };

    updateTodo(todo) = function {
    $http({
        method:'POST',
        url: '/api/task/',
        headers: {'Content-Type':'application/json','token': todo_token},
        data: {task_id: todo.task_id, status: todo.status,},
        }).then(function(response) {
        $scope.todos = response.data.data;
        $cookies.put('todo_token', response.data.token);
        $scope.loading = false;
    }

    todoList.archive = function() {
      var oldTodos = todoList.todos;
      todoList.todos = [];
      angular.forEach(oldTodos, function(todo) {
        if (!todo.done) todoList.todos.push(todo);
      });
    };
  });