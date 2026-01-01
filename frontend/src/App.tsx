import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createUser } from './api/users'

function App() {
  const [count, setCount] = useState(0)
  const [userName, setUserName] = useState("")
  const [userResult, setUserResult] = useState<string>("")

  // Function to handle creating a user
  const handleCreateUser = async () => {
    try {
      const user = await createUser({ name: userName })
      setUserResult(`User created with ID: ${user.id}`)
      setUserName("")
    } catch (err) {
      console.error(err)
      setUserResult("Error creating user")
    }
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>

      {/* New section for creating a user */}
      <div className="card" style={{ marginTop: "20px" }}>
        <input
          type="text"
          value={userName}
          placeholder="Enter name"
          onChange={(e) => setUserName(e.target.value)}
        />
        <button onClick={handleCreateUser} style={{ marginLeft: "10px" }}>
          Create User
        </button>
        {userResult && <p>{userResult}</p>}
      </div>

      <p className="read-the-docs">
        Atum
      </p>
    </>
  )
}

export default App
