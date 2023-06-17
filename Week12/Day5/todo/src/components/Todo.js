import React from 'react'

class Todo extends React.Component{
    constructor() {
        super();
        this.state = {
            todos: ['Not to die today', 'Drink some vodka'],
            newTodo: '',
            selectedTodoIndex: null
        }
    }

    handleMouseEnter = (index) => {
        this.setState({ selectedTodoIndex: index });
      };
    
    handleMouseLeave = () => {
        this.setState({ selectedTodoIndex: null });
      };



      handleClick = () => {
        const { todos, selectedTodoIndex } = this.state;
        if (selectedTodoIndex !== null) {
          const updatedTodos = [...todos];
          updatedTodos.splice(selectedTodoIndex, 1);
          this.setState({ todos: updatedTodos, selectedTodoIndex: null });
        }
      }; 





    handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            this.addTodo();
          }
        };

    handleInputChange = (event) => {
        this.setState({ newTodo: event.target.value });
        console.log("todos")
        };

    addTodo = () => {
        const { todos, newTodo } = this.state;
        if (newTodo.trim() !== '') {
            const updatedTodos = [...todos, newTodo]; 
            this.setState({ todos: updatedTodos, newTodo: '' }); 
            console.log(todos, updatedTodos, newTodo)
          }   

    }


    render() { 
        const { todos, newTodo, selectedTodoIndex } = this.state;
        return (
        <div>

            <h1>Todo's</h1>
            <div className='alltodos'>
            {todos.map((todo, index) => (
            <div
              className={`onetodo ${selectedTodoIndex === index ? 'selected' : ''}`}
              key={index}
              onMouseEnter={() => this.handleMouseEnter(index)}
              onMouseLeave={this.handleMouseLeave}
              onClick={this.handleClick}
              
            >
             <span style={{ textDecoration: selectedTodoIndex === index ? 'line-through' : 'none' }}>{todo}</span>

            </div>
          ))}
            </div>
            <div className="form">
            
                <label>Add a new todo:</label>
                <input type='text' value={newTodo} onChange={this.handleInputChange} onKeyDown={this.handleKeyPress} />
             
            </div>
        </div>
        )
    }       
}

export default Todo