import React from "react";

const UserItem = ({user}) => {
  return (
    <tr>
      <td>{user.username}</td>
      <td>{user.first_name}</td>
      <td>{user.last_name}</td>
      <td>{user.email}</td>
    </tr>
  )
};

const UsersList = ({users}) => {
  return (
    <div className="users_container center-block">
      <table className="table table-striped table-hover">
        <thead className="table-light">
        <tr>
          <th scope="col">Username</th>
          <th scope="col">First Name</th>
          <th scope="col">Last Name</th>
          <th scope="col">E-mail Address</th>
        </tr>
        </thead>
        <tbody>
        {users.map((user_) => <UserItem user={user_}/>)}
        </tbody>
      </table>
    </div>
  )
};

export default UsersList;