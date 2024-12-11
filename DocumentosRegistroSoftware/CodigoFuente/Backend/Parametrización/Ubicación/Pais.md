```
//ENTITY PAIS
package com.persona.Backend.Entity.Parameter.Ubicacion;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "pais")
public class Pais extends BaseEntity {

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "continente_id", nullable = false, unique = false)
	private Continente continenteId;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public Continente getContinenteId() {
		return continenteId;
	}

	public void setContinenteId(Continente continenteId) {
		this.continenteId = continenteId;
	}

	

}
// IREPOSITORY PAIS
package com.persona.Backend.IRepository.Parameter.Ubicacion;

import java.util.Optional;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Parameter.Ubicacion.Pais;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IPaisRepository extends IBaseRepository<Pais, Long>{

	 Optional<Pais> findByNombre(String nombre);
}
//ISERVICE PAIS
package com.persona.Backend.IService.Parameter.Ubicacion;

import com.persona.Backend.Entity.Parameter.Ubicacion.Pais;
import com.persona.Backend.IService.IBaseService;

public interface IPaisService extends IBaseService<Pais>{

	 Pais findByNombre(String nombre);
	 
	 
}
//SERVICE PAIS
package com.persona.Backend.Service.Parameter.Ubicacion;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.neovisionaries.i18n.CountryCode;
import com.persona.Backend.Entity.Parameter.Ubicacion.Pais;
import com.persona.Backend.IRepository.Parameter.Ubicacion.IPaisRepository;
import com.persona.Backend.IService.Parameter.Ubicacion.IDepartamentoService;
import com.persona.Backend.IService.Parameter.Ubicacion.IPaisService;
import com.persona.Backend.Service.BaseService;

@Service
public class PaisService extends BaseService<Pais> implements IPaisService {

	@Autowired
	private IPaisRepository paisRepository;

	@Autowired
	private IDepartamentoService departamentoService; // Servicio de Departamentos

	@Override
    public Pais findByNombre(String nombre) {
        return paisRepository.findByNombre(nombre).orElse(null);
        
	}       
        
}
//CONTROLLER PAIS
package com.persona.Backend.Controller.Parameter.Ubicacion;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Ubicacion.Pais;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/ubicacion/pais")
public class PaisController extends BaseController<Pais> {

}


```