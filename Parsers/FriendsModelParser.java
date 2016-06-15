import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

class FriendsModelParser {


		public FriendsModel parseFriendsModel(String json_object) {

			FriendsModel local_model = null;
			try {
					JSONObject jsobj = new JSONObject(json_object);

					local_model = new FriendsModel(jsobj.getString("name") , jsobj.getInt("id") );
 			} 
			catch (JSONException e){

 				 e.printStackTrace();
			}

			return local_model;
		}
			
}