import java.util.ArrayList;

class RootModel {

		public int age;
		public String about;
		public Boolean isActive;
		public String _id;
		public String gender;
		public String name;
		public String email;
		public String balance;
		public String company;
		public String registered;
		public String greeting;
		public String picture;
		public String eyeColor;
		public String address;
		public int index;
		public ArrayList<FriendsModel> friends;
		public String phone;
		public String favoriteFruit;
		public String guid;
		public ArrayList<Integer> tags;

public RootModel(int age, String about, Boolean isActive, String _id, String gender, String name, String email, String balance, String company, String registered, String greeting, String picture, String eyeColor, String address, int index, ArrayList<FriendsModel> friends, String phone, String favoriteFruit, String guid, ArrayList<Integer> tags) {

		this.age = age;
		this.about = about;
		this.isActive = isActive;
		this._id = _id;
		this.gender = gender;
		this.name = name;
		this.email = email;
		this.balance = balance;
		this.company = company;
		this.registered = registered;
		this.greeting = greeting;
		this.picture = picture;
		this.eyeColor = eyeColor;
		this.address = address;
		this.index = index;
		this.friends = friends;
		this.phone = phone;
		this.favoriteFruit = favoriteFruit;
		this.guid = guid;
		this.tags = tags;

	}

}