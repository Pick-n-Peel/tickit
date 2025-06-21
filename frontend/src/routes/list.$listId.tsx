import { createFileRoute } from '@tanstack/react-router'
import ListsTab from "./index.tsx";

export const Route = createFileRoute("/list/$listId")({
  component: ListDetailPage,
})


function ListDetailPage() {
  console.log(Route)

  const { listId } = Route.useParams()
  return (
    <div>
      <div>
        <ListsTab />
      </div>
      <div className="h-52" /> {/* 52 is approx 208px */}
      <div className="flex justify-center">
        List ID: {listId}
      </div>
    </div>
  );
}

export default ListDetailPage;
