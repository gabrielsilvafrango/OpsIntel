import { useState } from "react";
import { createUser } from "../api/users";

function Users() {
  const [name, setName] = useState("");
  const [result, setResult] = useState<string>("");

  async function handleSubmit() {
    try {
      const user = await createUser({ name });
      setResult(`Created user #${user.id}`);
    } catch (err) {
      setResult("Error creating user");
    }
  }

  return (
    <div style={{ padding: 20 }}>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
      />
      <button onClick={handleSubmit}>Create</button>
      <p>{result}</p>
    </div>
  );
}

export default Users;
