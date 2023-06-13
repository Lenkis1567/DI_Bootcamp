import React, { useState } from "react";

function Languages() {
    const [languages, setLanguages] = useState([
        { name: 'Php', votes: 0 },
        { name: 'Python', votes: 0 },
        { name: 'JavaScript', votes: 0 },
        { name: 'Java', votes: 0 }
      ]);
    
      const handleVote = (index) => {
        setLanguages((prevLanguages) => {
          const updatedLanguages = [...prevLanguages];
          updatedLanguages[index].votes += 1;
          return updatedLanguages;
        });
      };
    
      return (
        <div>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Votes</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {languages.map((language, index) => (
                <tr key={index}>
                  <td>{language.name}</td>
                  <td>{language.votes}</td>
                  <td>
                    <button onClick={() => handleVote(index)} style={{ color: 'green', padding: '5px', border: '0' }}>Click here</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    }
    
export default Languages;