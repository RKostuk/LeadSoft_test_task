import React from 'react';
import { Admin, Resource, List, Datagrid, TextField } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';

const dataProvider = jsonServerProvider('http://localhost:3001');

// panel admin
const AdminPanel = () => (
  <Admin dataProvider={dataProvider}>
    <Resource name="content" list={FileList} />
  </Admin>
);

// components admin panel
const FileList = (props) => (
  <List {...props}>
    <Datagrid>
      <TextField source="id" />
      <TextField source="end_user_id" />
      <TextField source="web_page_url" />
    </Datagrid>
  </List>
);

export default AdminPanel;
