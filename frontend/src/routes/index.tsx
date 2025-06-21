import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Outlet, useMatch, useNavigate } from "@tanstack/react-router";
import { useState } from "react";

export const Route = createFileRoute("/")({
  component: Index,
});

function ListButton({
  name,
  listId,
  selectedValue,
  onChange,
}: {
  name: string;
  listId: string;
  selectedValue: string;
  onChange: (value: string) => void;
  }) {
  const navigate = useNavigate()

  const selectedList = String(selectedValue) === String(listId)

  return (
    <label className="items-center cursor-pointer">
      <input
        type="radio"
        name={name}
        checked={selectedList}
        onChange={() => onChange(listId)}
        className="sr-only"
        onClick={() =>
          navigate({
            to: '/list/$listId',
            params: {listId: listId}
          })
        }
        // className="radio radio-accent"
      />
      <span className={`btn btn-wide w-full sm:w-48 ${
          selectedList ? "btn-accent" : "btn-soft"
        } `}
      >
      {name}
      </span>
    </label>
  );
}

function ListsTab(
) {
  const match = useMatch("/list/$listId");
  const selectedList = match?.params?.listId ?? '';

  const navigate = useNavigate();

  const listQuery = useQuery({
    queryKey: ['list'],
    queryFn: async () => {
      const response = await fetch('/api/list/')
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      return response.json()
    },
  });

  const handleChange = (listId: string) => {
    navigate({
      to: '/list/$listId',
      params: { listId }
    });
  };

  return (
    <div className="justify-center mt-10">
      <div className="flex justify-center space-x-0">
        {
          listQuery.data?.map((l) => (
            <ListButton
              key={l.id}
              listId={l.id}
              name={l.name}
              selectedValue={selectedList}
              onChange={handleChange} />)

          )
        }

      </div>
      <Outlet />
      </div>
  );
}

function Index() {

  return (
    <div>
      <ListsTab />
      <div className="h-52" /> {/* 52 is approx 208px */}
    <div className="flex flex-col size-full justify-center items-center gap-2">
    <h1 className="text-base-content/70">Welcome to TickIt.</h1>
    <p className="text-base-content/50">Select a list to get started.</p>
  </div>
  </div>
  );
}

export default ListsTab;
