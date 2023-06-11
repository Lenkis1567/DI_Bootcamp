import '../Exercise4.css';

const Exercise4 = () => { 
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
      };
return (
    <div> 
        <h1 style={style_header}>Cool header</h1>
        <p className="para">Paragraph</p>
        <form>
            <label> Name:
            <input type="text" />
            </label>
            <input type="submit" value="Submit" />
      </form>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
        <img src='/orch.jpg' alt='Orchid' />
        <a href ="https://en.wikipedia.org/wiki/Orchid">Orchids</a>
    </div>
)
}

export default Exercise4;