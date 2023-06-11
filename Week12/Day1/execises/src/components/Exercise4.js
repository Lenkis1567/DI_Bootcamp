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
        <img src='/orch.jpg' alt='Orchid' />
        <a href ="https://en.wikipedia.org/wiki/Orchid">Orchids</a>
    </div>
)
}

export default Exercise4;