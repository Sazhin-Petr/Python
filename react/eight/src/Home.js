function Home({ items, onCheckboxChange }){
     const selectedItems = items.filter(item => item.checked);

    return(
        <div style={{ 
            display: 'flex', 
            flexDirection: 'column', 
            alignItems: 'center',
            justifyContent: 'center',
        }}>
            <h2 style={{marginBottom: 60}}>Home Page</h2>
            <form>
                <fieldset style={{ border: 'none' }}>
                    <legend style={{ 
                        textAlign: 'center', 
                        fontWeight: 'bold', 
                        fontSize: '20px',
                        width: '100%',
                        marginBottom: "30"
                    }}>Shopping list</legend>
                    {items.map(item => (
                        <div key={item.id}>
                            <label style={{ 
                                color: item.checked ? 'blue' : 'black',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'space-between'
                            }}>
                                 <span style={{ display: 'flex', alignItems: 'center' }}>
                                    <input 
                                        type="checkbox" 
                                        checked={item.checked}
                                        onChange={() => onCheckboxChange(item.id)}
                                        style={{ marginRight: '8px' }}
                                    />
                                    {item.name}
                                </span>
                                <span style={{ 
                                    width: "100px",
                                    textAlign: 'center'
                                     }}>
                                    {item.checked ? '+' : '-'}
                                </span>
                            </label>
                             
                        </div>
                    ))}
                </fieldset>
            </form>
             {selectedItems.length > 0 && (
                
                <div>
                    <hr style={{ 
                        width: '300px', 
                        border: '1px solid #ccc', 
                        margin: '20px auto' 
                    }} />
                    <h3>Total Completed: {selectedItems.length}</h3>
                </div>
            )}
        </div>
    )
}

export default Home;